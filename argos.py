


import argostranslate.package
import argostranslate.translate

#from_code = "en"
#to_code = "es"

# Download and install Argos Translate package
#argostranslate.package.update_package_index()
#available_packages = argostranslate.package.get_available_packages()
#package_to_install = next(
#    filter(
#        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
#    )
#)
#argostranslate.package.install_from_path(package_to_install.download())

# Translate
#translatedText = argostranslate.translate.translate("Hello World", from_code, to_code)
#print(translatedText)


#import argostranslate.translate
#import argostranslate.package
#
sss = 'わ か っ て も ら え る だ ろ う か ?'
#
from_code = "ja"
to_code = "en"
#
argostranslate.package.install_from_path('./translate-ja_en-1_1.argosmodel')
#translatedText = argostranslate.translate.translate(sss, from_code, to_code)
translatedText = argostranslate.translate.translate('わかってもらえるだろうか?', from_code, to_code)
#translatedText = argostranslate.translate.translate('あたしには', from_code, to_code)
#
print(translatedText)
