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
            // this.data = [];
        },
        /**
         *
         * @override
         */
        start: async function () {
            const dept_id = (this.target.dataset.tempName && JSON.parse(this.target.dataset.tempName)[0].id) || -1;
            const data = await this.rpc("/website/departments", {dept_id: dept_id});
            debugger;
            document.querySelector("#temp_data").replaceChildren(renderToElement("department-data", {data: data}));
        },
    });
publicWidget.registry.s_employee = EmployeeSnippet;
export default EmployeeSnippet;
