/** @odoo-module **/
import options from "@web_editor/js/editor/snippets.options";

options.registry.s_employee_options = options.Class.extend({
    async willStart() {
        const _super = this._super.bind(this);
        return _super(...arguments);
    },
});

