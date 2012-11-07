# Iremos cadastrar no catalogo se tem imagem no banner ou não 
# por isso faremos os if's através deste script

if context.Type() == 'Banner':
    return bool(context.getImagem_banner())
    
return False

