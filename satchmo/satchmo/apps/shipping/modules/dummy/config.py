# from livesettings.values import DecimalValue
# from livesettings.functions import config_register_list,config_get_group,config_get
# 
# SHIP_MODULES = config_get('SHIPPING', 'MODULES')
# SHIP_MODULES.add_choice(('shipping.modules.dummy', 'Dummy Shipping'))
# SHIPPING_GROUP = config_get_group('SHIPPING')
# 
# config_register_list(
# DecimalValue(SHIPPING_GROUP,
#     'FLAT_RATE',
#     description=_("Flat shipping"),
#     requires=SHIPPING_ACTIVE,
#     requiresvalue='shipping.modules.flat',
#     default="4.00"),
# )
