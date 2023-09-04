import streamlit as st
import numpy as np
import pandas as pd
# import requests

# Crear un DataFrame de ejemplo con tasas de cambio

# URL a la que deseas enviar la solicitud GET
# url = 'http://api.currencylayer.com/live?access_key='+llaveAcceso

# Realiza la solicitud GET
# response = requests.get(url)

# Verifica el código de estado de la respuesta (200 significa éxito)
#if response.status_code == 200:
#    data = response.json()  # Si la respuesta es JSON
#    print(data)
#else:
#    print('La solicitud GET falló con el código de estado:', response.status_code)

# De momento se utilizara un json statico para no sobreconsultar la api
        
data = {
    'Divisa': ['COP: Peso colombiano', 'USD: Dólar estadounidense', 'AED: Dirham de los Emiratos Árabes Unidos', 'AFN: Afgani afgano', 'ALL: Lek albanés', 'AMD: Dram armenio', 'ANG: Florín antillano neerlandés', 'AOA: Kwanza angoleño', 'ARS: Peso argentino', 'AUD: Dólar australiano', 'AWG: Florín arubeño', 'AZN: Manat azerbaiyano', 'BAM: Marco convertible de Bosnia y Herzegovina', 'BBD: Dólar de Barbados', 'BDT: Taka de Bangladesh', 'BGN: Lev búlgaro', 'BHD: Dinar bahreiní', 'BIF: Franco burundés', 'BMD: Dólar de Bermudas', 'BND: Dólar de Brunéi', 'BOB: Boliviano boliviano', 'BRL: Real brasileño', 'BSD: Dólar bahameño', 'BTC: Bitcoin', 'BTN: Ngultrum butanés', 'BWP: Pula de Botsuana', 'BYN: Rublo bielorruso', 'BYR: Rublo bielorruso (obsoleto)', 'BZD: Dólar beliceño', 'CAD: Dólar canadiense', 'CDF: Franco congoleño', 'CHF: Franco suizo', 'CLF: Unidad de fomento chilena', 'CLP: Peso chileno', 'CNY: Yuan chino', 'CRC: Colón costarricense', 'CUC: Peso cubano convertible', 'CUP: Peso cubano', 'CVE: Escudo caboverdiano', 'CZK: Corona checa', 'DJF: Franco yibutiano', 'DKK: Corona danesa', 'DOP: Peso dominicano', 'DZD: Dinar argelino', 'EGP: Libra egipcia', 'ERN: Nakfa eritreo', 'ETB: Birr etíope', 'EUR: Euro', 'FJD: Dólar de Fiyi', 'FKP: Libra malvinense', 'GBP: Libra esterlina', 'GEL: Lari georgiano', 'GGP: Libra de Guernsey', 'GHS: Cedi ghanés', 'GIP: Libra de Gibraltar', 'GMD: Dalasi gambiano', 'GNF: Franco guineano', 'GTQ: Quetzal guatemalteco', 'GYD: Dólar guyanés', 'HKD: Dólar de Hong Kong', 'HNL: Lempira hondureño', 'HRK: Kuna croata', 'HTG: Gourde haitiano', 'HUF: Forinto húngaro', 'IDR: Rupia indonesia', 'ILS: Nuevo séquel israelí', 'IMP: Libra de la Isla de Man', 'INR: Rupia india', 'IQD: Dinar iraquí', 'IRR: Rial iraní', 'ISK: Corona islandesa', 'JEP: Libra de Jersey', 'JMD: Dólar jamaicano', 'JOD: Dinar jordano', 'JPY: Yen japonés', 'KES: Chelín keniano', 'KGS: Som kirguís', 'KHR: Riel camboyano', 'KMF: Franco comorense', 'KPW: Won norcoreano', 'KRW: Won surcoreano', 'KWD: Dinar kuwaití', 'KYD: Dólar de las Islas Caimán', 'KZT: Tenge kazajo', 'LAK: Kip laosiano', 'LBP: Libra libanesa', 'LKR: Rupia de Sri Lanka', 'LRD: Dólar liberiano', 'LSL: Loti lesothense', 'LTL: Litas lituano', 'LVL: Lats letón', 'LYD: Dinar libio', 'MAD: Dírham marroquí', 'MDL: Leu moldavo', 'MGA: Ariary malgache', 'MKD: Denar macedonio', 'MMK: Kyat birmano', 'MNT: Tugrik mongol', 'MOP: Pataca de Macao', 'MRO: Uquiya mauritana', 'MUR: Rupia de Mauricio', 'MVR: Rufiyaa maldiva', 'MWK: Kwacha malauí', 'MXN: Peso mexicano', 'MYR: Ringgit malayo', 'MZN: Metical mozambiqueño', 'NAD: Dólar namibio', 'NGN: Naira nigeriana', 'NIO: Córdoba nicaragüense', 'NOK: Corona noruega', 'NPR: Rupia nepalesa', 'NZD: Dólar neozelandés', 'OMR: Rial omaní', 'PAB: Balboa panameño', 'PEN: Sol peruano', 'PGK: Kina de Papúa Nueva Guinea', 'PHP: Peso filipino', 'PKR: Rupia pakistaní', 'PLN: Zloty polaco', 'PYG: Guaraní paraguayo', 'QAR: Riyal qatarí', 'RON: Leu rumano', 'RSD: Dinar serbio', 'RUB: Rublo ruso', 'RWF: Franco ruandés', 'SAR: Riyal saudí', 'SBD: Dólar de las Islas Salomón', 'SCR: Rupia de Seychelles', 'SDG: Libra sudanesa', 'SEK: Corona sueca', 'SGD: Dólar singapurense', 'SHP: Libra de Santa Elena', 'SLE: Leone sierraleonés', 'SLL: Leone de Sierra Leona', 'SOS: Chelín somalí', 'SRD: Dólar surinamés', 'STD: Dobra de Santo Tomé y Príncipe', 'SSP: Libra sursudanesa', 'SYP: Libra siria', 'SZL: Lilangeni suazi', 'THB: Baht tailandés', 'TJS: Somoni tayiko', 'TMT: Manat turcomano', 'TND: Dinar tunecino', "TOP: Pa'anga tongano", 'TRY: Lira turca', 'TTD: Dólar de Trinidad y Tobago', 'TWD: Nuevo dólar taiwanés', 'TZS: Chelín tanzano', 'UAH: Grivna ucraniana', 'UGX: Chelín ugandés', 'UYU: Peso uruguayo', 'UZS: Som uzbeko', 'VEF: Bolívar venezolano', 'VES: Bolívar soberano venezolano', 'VND: Dong vietnamita', 'VUV: Vatu vanuatuense', 'WST: Tala samoano', 'XAF: Franco CFA de África Central', 'XAG: Plata (en onzas troy)', 'XAU: Oro (en onzas troy)', 'XCD: Dólar del Caribe Oriental', 'XDR: Derechos especiales de giro del FMI', 'XOF: Franco CFA de África Occidental', 'XPF: Franco CFP', 'YER: Rial yemení', 'ZAR: Rand sudafricano', 'ZMK: Kwacha zambiano (obsoleto)', 'ZMW: Kwacha zambiano', 'ZWL: Dólar zimbabuense'],
    'codigos': ['COP', 'USD','AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STD', 'SSP', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL'],
    'Tasa de Cambio a USD': [4058.46, 1, 3.673049, 73.44727, 100.179703, 386.200509, 1.80379, 825.022498, 350.037987, 1.547688, 1.8, 1.701853, 1.811345, 2.020468, 110.025469, 1.811739, 0.376904, 2841.924876, 1, 1.354546, 6.914564, 4.937099, 1.000871, 3.8680689e-05, 82.738041, 13.58887, 2.526326, 19600, 2.017041, 1.35945, 2484.999799, 0.884515, 0.031088, 857.810006, 7.272503, 537.446158, 1, 26.5, 102.120861, 22.355031, 177.719715, 6.90324, 56.986707, 136.702716, 30.898843, 15, 55.307625, 0.926305, 2.25995, 0.794126, 0.79175, 2.634981, 0.794126, 11.40727, 0.794126, 60.849796, 8594.321708, 7.880528, 209.520722, 7.83395, 24.647078, 6.8828, 135.557738, 354.274496, 15223.45, 3.81395, 0.794126, 82.72855, 1310.488539, 42274.99973, 133.297886, 0.794126, 154.442551, 0.708097, 146.482961, 144.820377, 88.2546, 4175.852678, 455.00015, 899.995566, 1318.600246, 0.30837, 0.833897, 458.865478, 19735.123871, 15040.055568, 320.222274, 185.999762, 18.510144, 2.95274, 0.60489, 4.820482, 10.179393, 17.861542, 4513.876024, 56.987355, 2101.782208, 3474.158681, 8.07548, 356.999828, 46.609698, 15.438566, 1067.471933, 17.174958, 4.654974, 63.24995, 18.509997, 757.489907, 36.617109, 10.63911, 132.403942, 1.684069, 0.385003, 1.000695, 3.704469, 3.663564, 56.807498, 306.634647, 4.143096, 7276.684418, 3.641003, 4.581901, 108.635008, 96.874951, 1195.023899, 3.750545, 8.36952, 13.352169, 600.753858, 11.00757, 1.355002, 1.21675, 22.280078, 19750.000033, 568.498038, 38.596498, 20697.981008, 601.501599, 13001.615103, 18.911408, 35.259955, 10.992359, 3.51, 3.092496, 2.387102, 26.754197, 6.781199, 31.923398, 2507.132535, 36.962837, 3722.157907, 37.629081, 12125.955082, 3272526.660879, 32.138323, 24085, 120.931765, 2.73571, 607.61514, 0.041692, 0.000516, 2.70255, 0.752529, 607.61514, 110.720079, 250.35018, 19.11905, 9001.198224, 20.338967, 321.999592]
}

df = pd.DataFrame(data)

# Configurar la aplicación Streamlit
st.title("Cambio de Divisas")

# Obtener la divisa de origen y destino
divisa_origen = st.selectbox("Selecciona la divisa de origen:", df['Divisa'].tolist())
divisa_destino = st.selectbox("Selecciona la divisa de destino:", df['Divisa'].tolist())

# Ingresar el monto a cambiar
monto_origen = st.number_input(f"Ingrese el monto en {divisa_origen}:", min_value=0.0)

# Calcular el monto en la divisa de destino
codigo_origen= df.loc[df['Divisa'] == divisa_origen, 'codigos'].values[0]
codigo_destino= df.loc[df['Divisa'] == divisa_destino, 'codigos'].values[0]
tasa_origen = df.loc[df['Divisa'] == divisa_origen, 'Tasa de Cambio a USD'].values[0]
tasa_destino = df.loc[df['Divisa'] == divisa_destino, 'Tasa de Cambio a USD'].values[0]
monto_destino = (monto_origen / tasa_origen) * tasa_destino

st.write(f"{monto_origen} {codigo_origen} equivale a {monto_destino} {codigo_destino}")
