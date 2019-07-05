VIDEO_CHOOSER_MODAL_ONLOAD_HANDLERS = {
  'chooser': function(modal, jsonData) {
      var searchUrl = $('form.video-search', modal.body).attr('action');

      function ajaxifyLinks (context) {
          $('a.video-choice', context).on('click', function(e) {
              modal.loadUrl(this.href);
              e.preventDefault();
          });

          $('.pagination a', context).on('click', function(e) {
              var page = this.getAttribute("data-page");
              setPage(page);
              e.preventDefault();
          });
      }

      function fetchResults(requestData) {
          $.ajax({
              url: searchUrl,
              data: requestData,
              success: function(data, status) {
                  $('#search-results').html(data);
                  ajaxifyLinks($('#search-results'));
              }
          });
      }

      function search() {
          fetchResults({
              q: $('#id_q').val(),
              collection_id: $('#collection_chooser_collection_id').val()
          });
          return false;
      }

      function setPage(page) {
          params = {p: page};
          if ($('#id_q').val().length){
              params['q'] = $('#id_q').val();
          }
          params['collection_id'] = $('#collection_chooser_collection_id').val();
          fetchResults(params);
          return false;
      }

      ajaxifyLinks(modal.body);

      $('form.video-upload', modal.body).on('submit', function() {
          var formdata = new FormData(this);

          if ($('#id_title', modal.body).val() == '') {
              var li = $('#id_title', modal.body).closest('li');
              if (!li.hasClass('error')) {
                  li.addClass('error');
                  $('#id_title', modal.body).closest('.field-content').append('<p class="error-message"><span>This field is required.</span></p>')
              }
              setTimeout(cancelSpinner, 500);
          } else {
              $.ajax({
                  url: this.action,
                  data: formdata,
                  processData: false,
                  contentType: false,
                  type: 'POST',
                  dataType: 'text',
                  success: modal.loadResponseText,
                  error: function(response, textStatus, errorThrown) {
                      message = jsonData['error_message'] + '<br />' + errorThrown + ' - ' + response.status;
                      $('#upload').append(
                          '<div class="help-block help-critical">' +
                          '<strong>' + jsonData['error_label'] + ': </strong>' + message + '</div>');
                  }
              });
          }

          return false;
      });

      $('form.video-search', modal.body).on('submit', search);

      $('#id_q').on('input', function() {
          clearTimeout($.data(this, 'timer'));
          var wait = setTimeout(search, 200);
          $(this).data('timer', wait);
      });
      $('#collection_chooser_collection_id').on('change', search);
  },
  'video_chosen': function(modal, jsonData) {
      modal.respond('videoChosen', jsonData['result']);
      modal.close();
  },
  'select_format': function(modal) {
      $('form', modal.body).on('submit', function() {
          var formdata = new FormData(this);

          $.post(this.action, $(this).serialize(), modal.loadResponseText, 'text');

          return false;
      });
  }
};
