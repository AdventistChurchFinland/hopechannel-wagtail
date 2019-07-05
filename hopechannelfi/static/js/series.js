(function() {
    const BREAKPOINTS = {
        xs: 480,
        sm: 768,
        md: 1024,
        lg: 1200,
    };
    const COLS = {
        xs: 2,
        sm: 3,
        md: 6,
        lg: 6,
    };
    
    const seriesContainer = document.getElementById('series');
    const series = seriesContainer && seriesContainer.children;

    let currentBreakpoint = getCurrentBreakPoint();
    let currentOpenElement = null;
    let currentOpenIndex = -1;
    let currentInfoElement = null;

    function throttle(func, limit) {
        let lastFunc;
        let lastRan;
        return function() {
            const context = this;
            const args = arguments;
            if (!lastRan) {
                func.apply(context, args);
                lastRan = Date.now();
            } else {
                clearTimeout(lastFunc);
                lastFunc = setTimeout(function() {
                    if ((Date.now() - lastRan) >= limit) {
                        func.apply(context, args);
                        lastRan = Date.now();
                    }
                }, limit - (Date.now() - lastRan));
            }
        }
    }

    function getCurrentBreakPoint() {
        let currentBreakpoint = 'xs';
        for (let breakpoint in BREAKPOINTS) {
            if (BREAKPOINTS.hasOwnProperty(breakpoint)) {
                if (window.innerWidth >= BREAKPOINTS[breakpoint]) {
                    currentBreakpoint = breakpoint;
                }
            }
        }
        return currentBreakpoint;
    }

    function getInsertIndex(currentIndex, divider) {
        const columnIndex = currentIndex % divider;
        return currentIndex - columnIndex + divider;
    }

    function toggleInfo(event) {
        event.preventDefault();

        const seriesItem = event.currentTarget.parentElement;

        if (seriesItem.classList.contains('series-menu--open')) {
            close(seriesItem);
        } else {
            if (currentOpenElement) {
                close(currentOpenElement);
                window.setTimeout(function() {
                    open(seriesItem);
                }, 200);
            } else {
                open(seriesItem);
            }
        }
    }

    function open(element) {
        currentOpenElement = element;
        currentOpenIndex = parseInt(element.getAttribute('data-index'), 10);

        const infoEl = element.getElementsByClassName('series-menu__info')[0];
        const instertIndex = getInsertIndex(currentOpenIndex, COLS[currentBreakpoint]);
        const infoClone = infoEl.cloneNode(true);
        
        element.classList.add('series-menu--open');
        currentInfoElement = seriesContainer.insertBefore(infoClone, series[instertIndex]);
        infoClone.style.height = infoClone.firstElementChild.offsetHeight + 'px';
    }

    function close(element){
        currentInfoElement.style.height = '0px';
        window.setTimeout(function() {
            seriesContainer.removeChild(currentInfoElement);
            element.classList.remove('series-menu--open');
    
            currentOpenElement = null;
            currentOpenIndex = -1;
            currentInfoElement = null;
        }, 200);
    }

    function refresh() {
        const breakpoint = getCurrentBreakPoint()
        if (currentBreakpoint !== breakpoint) {
            currentBreakpoint = breakpoint;
            if (currentOpenElement) {
                const stashedOpenIndex = currentOpenIndex;
                close(currentOpenElement);
                open(series[stashedOpenIndex]);
            }
        }
    }

    if (series) {
        window.addEventListener('resize', throttle(refresh, 500));

        Array.prototype.forEach.call(series, function(el, index) {
            el.setAttribute('data-index', index);
            const showMore = el.getElementsByTagName('button')[0];
            showMore.addEventListener('click', toggleInfo);
        })
    }
})();