function openerp_pos_models_ex(instance, module){
    
    _super = module.PosModel
    module.PosModel = module.PosModel.extend({
        initialize : function(session, attributes) {
            _super.prototype.initialize.call(this,session, attributes)
            this.db.clear('products','categories','customers');
            this.set({'customers':new module.CustomerCollection()});
        },
        load_server_data : function(){
            self = this
            loaded = _super.prototype.load_server_data.call(this)
                .then(function(){
                     return self.fetch('res.partner', ['name','vat','email',
                        'phone','mobile','street','street2'],[['customer', '=', true]]);
                }).then(function(customers){
                    self.db.add_customers(customers);
                })
            return loaded
        }
    })
    
    module.Customer = Backbone.Model.extend({
    });

    module.CustomerCollection = Backbone.Collection.extend({
        model: module.Customer,
    });
}