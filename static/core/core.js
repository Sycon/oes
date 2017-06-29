/**
 * Created by chimaobi on 4/26/17.
 */

new Vue({
    el: '#myapp',
    data: {
        name: "Chimaobi",
        up: 0,
        sub: 0,
        dsub: 0,
        ichev: true,
    },
    delimiters: ['${', '}'],
    methods: {
        chev: function () {
            this.ichev = !this.ichev
        }
    },
})
