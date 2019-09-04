(function() {
    const BREAKPOINTS = {
        xs: 480,
        sm: 768,
        md: 1024,
        lg: 1200,
    };

    const scrollers = document.getElementsByClassName('scroller');

    function Scroller(element) {
        this.scroller = element.getElementsByClassName('scroller__items')[0];

        const itemCount = this.scroller.children.length

        // Having to build perPage option the old way for IE11
        const siemaPerPageOption = {};
        siemaPerPageOption[BREAKPOINTS.xs] = Math.min(2, itemCount);
        siemaPerPageOption[BREAKPOINTS.md] = Math.min(3, itemCount);
        siemaPerPageOption[BREAKPOINTS.lg] = Math.min(4, itemCount);

        const siemaOptions = {
            selector: this.scroller,
            perPage: siemaPerPageOption,
            loop: true
        }

        this.siema = new Siema(siemaOptions);
        this.prev = this.prev.bind(this);
        this.next = this.next.bind(this);

        this.prevEl = element.getElementsByClassName('scroller__advance--prev')[0];
        this.nextEl = element.getElementsByClassName('scroller__advance--next')[0];

        this.prevEl.addEventListener('click', this.prev);
        this.nextEl.addEventListener('click', this.next);
    }

    Scroller.prototype.prev = function() {
        this.siema.prev();
    }

    Scroller.prototype.next = function() {
        this.siema.next();
    }

    if (Siema) {
        Array.prototype.forEach.call(scrollers, function(el, index) {
            new Scroller(el);
        })
    }
})();