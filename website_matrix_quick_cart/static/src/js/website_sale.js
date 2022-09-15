odoo.define('website_matrix_quick_cart.website_sale', function(require) {
"use strict";
var publicWidget = require('web.public.widget');
var WebsiteSale = require('website_sale.website_sale').WebsiteSale;
var wSaleUtils = require('website_sale.utils');
WebsiteSale.include({
    events: _.extend({}, WebsiteSale.prototype.events || {}, {
        'click #matrix_add_to_cart': '_onClickMatrix',
    }),
    _onClickMatrix: async function(ev){
        var datas = [];
        var products = $(ev.currentTarget).closest('.js_main_product').find('.knk_matrix_table div .row.product_variant');
        var elmets = $(ev.currentTarget).closest('.js_main_product').find(".knk_matrix_table div .row.product_variant .cart_relative input[name='add_qty[]']");
        if(elmets != undefined && elmets.length){
            _.each(elmets, function(elmt, index){
                if($(elmt).val() != '' && $(elmt).val() != '0' && $.isNumeric($(elmt).val())){
                    var product_id = parseInt($(elmt).closest('.row').attr('data-product_id'), 10);
                    var qty = parseInt($(elmt).val(), 10);
                    datas.push({
                        'product_id' : product_id,
                        'qty' : qty,
                    })
                }
            });
        }
        if (datas != undefined && datas.length != 0) {
            this._rpc({
                route: "/shop/matrix/cart",
                params: {
                    datas: datas,
                },
            }).then(function (data) {
                if (data) {
                    return window.location = '/shop/cart';
                }

                wSaleUtils.updateCartNavBar(data);
                wSaleUtils.showWarning(data.warning);
            });
        }
    }
});
});