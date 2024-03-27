/** @odoo-module */
import publicWidget from "@web/legacy/js/public/public_widget";
import { renderToElement } from "@web/core/utils/render";

var EmployeeSnippet = publicWidget.Widget.extend({
        selector: '.dynamic_snippet_employee',
        /**
         *
         * @constructor
         */
        init: function () {
            this._super.apply(this, arguments);
            this.rpc = this.bindService("rpc");
            this.data = [];
        },
        /**
         *
         * @override
         */
        start: async function () {
            console.log('gfdfggf')
            this.data = await this.rpc("/website/departments")
            console.log(this.$("#temp_data"))
            console.log(this.data)
            this.$("#temp_data").replaceWith(renderToElement("department-data", {data: this.data}));
        },
    });
publicWidget.registry.s_employee = EmployeeSnippet;
export default EmployeeSnippet;
