(function() {
    if (window.cookieconsent) {
        function initialiseCookieConsent() {
            window.cookieconsent.initialise({
                "palette": {
                    "popup": {
                        "background": "#002244"
                    },
                    "button": {
                        "background": "#f1d600"
                    }
                },
                "theme": "classic",
                "position": "top",
                "static": "true",
                "content": {
                    "message": "Sivustomme käyttää Vimeo-videopalvelun evästeitä. Jatkamalla sivuston käyttöä hyväksyt evästeet. Voit lukea Vimeon evästeiden käytöstä",
                    "dismiss": "Hyväksyn",
                    "link": "täältä.",
                    "href": "https://vimeo.com/cookie_policy"
                }
            });
        }

        window.addEventListener("load", initialiseCookieConsent);
    }
})();