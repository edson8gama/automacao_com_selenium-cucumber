from behave import given, when, then

# Variável com a URL do site que será interagido.
base_url = 'http://sampleapp.tricentis.com/101/app.php'

# Variáveis com os elementos que será interagido na página
element_menu = 'nav_automobile'
element_make_field = ('make', "//option[. = 'Renault']")
element_engineperformance_field = ('engineperformance', '200')
element_dateofmanufacture_field = ('dateofmanufacture', '01/01/2010')
element_numberofseats_field = ('numberofseats', "//option[. = '5']")
element_fuel_field = ('fuel', "//option[. = 'Other']")
element_listprice_field = ('listprice', '20000')
element_annualmileage_field = ('annualmileage', '400')
element_next_button = 'nextenterinsurantdata'


@given(u'que acessei a pagina de cadastro do site para seguro')
def step_impl(context):
    context.web.get(base_url)


@when(u'clico no menu Automobile')
def step_impl(context):
    context.web.find_element_by_id(element_menu).click()


@when(u'preencho campo Make')
def step_impl(context):
    context.element_make_field = context.web.find_element_by_id(element_make_field[0])
    context.element_make_field.find_element_by_xpath(element_make_field[1])


@when(u'preencho campo Engine Performance')
def step_impl(context):
    context.web.find_element_by_id(element_engineperformance_field[0]).send_keys(element_engineperformance_field[1])


@when(u'preencho campo Date of Manufacture')
def step_impl(context):
    context.web.find_element_by_id(element_dateofmanufacture_field[0]).send_keys(element_dateofmanufacture_field[1])


@when(u'preencho campo Number of Seats')
def step_impl(context):
    context.element_numberofseats_field = context.web.find_element_by_id(element_numberofseats_field[0])
    context.element_numberofseats_field.find_element_by_xpath(element_numberofseats_field[1])


@when(u'preencho campo Fuel Type')
def step_impl(context):
    context.element_fuel_field = context.web.find_element_by_id(element_fuel_field[0])
    context.element_fuel_field.find_element_by_xpath(element_fuel_field[1])


@when(u'preencho campo List Price')
def step_impl(context):
    context.web.find_element_by_id(element_listprice_field[0]).send_keys(element_listprice_field[1])


@when(u'preencho campo Annual Mileage')
def step_impl(context):
    context.web.find_element_by_id(element_annualmileage_field[0]).send_keys(element_annualmileage_field[1])


@then(u'clico para ir para o proximo formulario')
def step_impl(context):
    context.web.find_element_by_id(element_next_button).click()
