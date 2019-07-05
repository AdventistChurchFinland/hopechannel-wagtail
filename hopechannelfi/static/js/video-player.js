(function() {
    function Modal(videoId) {
        this.open = this.open.bind(this);
        this.close = this.close.bind(this);
        this.onKeyDown = this.onKeyDown.bind(this);

        this.docFragment = document.createDocumentFragment();
        this.modalBackground = this.buildModalBackground();
        this.modal = this.buildModal(videoId);

        this.docFragment.appendChild(this.modalBackground);
        this.docFragment.appendChild(this.modal);

        this.open();
    }

    Modal.prototype.buildModalBackground = function() {
        const modalBackgroundEl = document.createElement('div');
        modalBackgroundEl.classList.add('modal__background');
        modalBackgroundEl.addEventListener('click', this.close);
        return modalBackgroundEl;
    }

    Modal.prototype.buildModal = function(videoId) {
        const modalEl = document.createElement('div');
        modalEl.classList.add('modal');

        const closeEl = document.createElement('button');
        closeEl.classList.add('modal__close');
        closeEl.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm0 14.5a6.5 6.5 0 1 1 0-13 6.5 6.5 0 0 1 0 13z"/><path d="M10.5 4L8 6.5 5.5 4 4 5.5 6.5 8 4 10.5 5.5 12 8 9.5l2.5 2.5 1.5-1.5L9.5 8 12 5.5z"/></svg>';
        closeEl.addEventListener('click', this.close);

        const videoContainerEl = document.createElement('div');
        videoContainerEl.classList.add('modal__video-container');

        const videoEl = document.createElement('iframe');
        videoEl.setAttribute('allowFullScreen', '');
        videoEl.setAttribute('mozallowfullscreen', '');
        videoEl.setAttribute('webkitAllowFullScreen', '');
        videoEl.setAttribute('frameborder', '0');
        videoEl.setAttribute('src', 'https://player.vimeo.com/video/' + videoId + '?autoplay=1&dnt=1');

        videoContainerEl.appendChild(videoEl);

        modalEl.appendChild(closeEl);
        modalEl.appendChild(videoContainerEl);

        return modalEl;
    }

    Modal.prototype.open = function() {
        document.body.appendChild(this.docFragment);
        document.body.style.overflow = 'hidden';
        window.addEventListener('keydown', this.onKeyDown);
    }

    Modal.prototype.close = function() {
        window.removeEventListener('keydown', this.onKeyDown);
        document.body.removeChild(this.modal);
        document.body.removeChild(this.modalBackground);
        document.body.style.overflow = 'auto';
    }

    Modal.prototype.onKeyDown = function(event) {
        if (event.keyCode === 27) {
            this.close();
        }
    }

    function onPlay(event) {
        if (event.target.classList.contains('play')) {
            const videoId = event.target.getAttribute('data-video-id');
            const modal = new Modal(videoId);
        }
    }

    window.addEventListener('click', onPlay);

})();