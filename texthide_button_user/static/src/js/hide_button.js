odoo.define('hide_button.HideButton', function (require) {
    "use strict";

    var WebClient = require('web.WebClient');
    var session = require('web.session');

    WebClient.include({
        show_application: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                // Check for hidden buttons after UI is loaded
                self.check_hidden_buttons();
            });
        },
        
        check_hidden_buttons: function () {
            var self = this;
            // Use rpc to get hidden buttons for current user
            this._rpc({
                model: 'hide.button.rule',
                method: 'get_hidden_buttons_for_user',
                args: [session.uid],
            }).then(function (hidden_buttons) {
                self.hide_buttons(hidden_buttons);
            });
        },
        
        hide_buttons: function (hidden_buttons) {
            var self = this;
            // Function to hide buttons
            function hideSpecificButtons() {
                hidden_buttons.forEach(function (button) {
                    // Multiple selectors to catch different button types
                    var selectors = [
                        `button[name="${button.button_name}"]`,
                        `button[data-name="${button.button_name}"]`,
                        `button:contains("${button.button_name}")`,
                        `.oe_button[name="${button.button_name}"]`,
                        `a[name="${button.button_name}"]`
                    ];
                    
                    selectors.forEach(function (selector) {
                        var buttons = document.querySelectorAll(selector);
                        buttons.forEach(function (btn) {
                            btn.style.display = 'none';
                        });
                    });
                });
            }
            
            // Initial hide
            hideSpecificButtons();
            
            // Use MutationObserver to watch for DOM changes
            var observer = new MutationObserver(function (mutations) {
                mutations.forEach(function (mutation) {
                    if (mutation.addedNodes.length > 0) {
                        hideSpecificButtons();
                    }
                });
            });
            
            // Start observing
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        }
    });
});
