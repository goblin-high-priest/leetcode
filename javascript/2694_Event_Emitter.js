class EventEmitter {
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    constructor() {
        this.events = new Map();
    }

    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) {
            this.events.set(eventName, [])
        }

        this.events.get(eventName).push(callback);

        return {
            unsubscribe: () => {
                const callbacks = this.events.get(eventName) || []

                const remaining = callbacks.filter(
                    fn => fn !== callback
                );

                if (remaining.length === 0) {
                    this.events.delete(eventName);
                } else {
                    this.events.set(eventName, remaining);
                }
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const callbacks = this.events.get(eventName) || [];
        const currentCallbacks = callbacks.slice();
        return currentCallbacks.map(callback => callback(...args));
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
