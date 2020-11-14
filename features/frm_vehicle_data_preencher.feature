#language: pt
Funcionalidade: Formulário "Enter Vehicle data"

    '''
    Eu como um possível cliente da Tricentis
    Quero acessar a página de seguro de automóveis
    Para fazer o preenchimento primeiramente do formulário Enter Vehicle Data
    '''

    Cenario: Preenchimento do formulario Enter Vehicle Data para automoveis
    Dado que acessei a pagina de cadastro do site para seguro
    Quando clico no menu Automobile
    E preencho campo Make
    E preencho campo Engine Performance
    E preencho campo Date of Manufacture
    E preencho campo Number of Seats
    E preencho campo Fuel Type
    E preencho campo List Price
    E preencho campo Annual Mileage
    Então clico para ir para o proximo formulario