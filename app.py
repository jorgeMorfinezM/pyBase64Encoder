# -*- coding: utf-8 -*-
"""
Requires Python 3.0 or later
"""

__author__ = "Jorge Morfinez Mojica (jorge.morfinez.m@gmail.com)"
__copyright__ = "Copyright 2019, Jorge Morfinez Mojica"
__license__ = "Apache 2.0"
__history__ = """ """
__version__ = "1.19.I11.Prod ($Rev: 3 $)"


import base64


# Metodo para leer un XML desde un archivo almacenado en cualquier directorio:
def read_xml_from_file_to_encode():
    pass
    # se setea el nombre del archivo con su directorio en una variable,
    # en este caso el archivo esta dentro del proyecto
    _file_name = 'xml_solo.xml'

    _file = open(_file_name, 'rb')
    _data = _file.read()
    _file.close()

    byte_array = xml_docto_base64_encoded(_data.decode())

    return byte_array


# Metodo principal para encodear a base64
def xml_docto_base64_encoded(self):
    pass
    xml_string = self

    xml_string = xml_string.replace("\n", "").replace("b'", "").replace("'", "")

    xml_to_bytes = bytes(xml_string, 'utf-8')

    xml_decoded = xml_to_bytes.decode('utf-8')

    xml_decoded = xml_decoded.replace("b'", "")
    xml_decoded = xml_decoded.replace("'", "")

    xml_base64_encodeaded = base64.b64encode(bytes(xml_decoded, 'utf-8'))

    xml_base64_encodeaded = xml_base64_encodeaded.decode('utf-8')

    return xml_base64_encodeaded


def main():
    pass
    """Fase 1: 
       
        Leer un XML en cadena de caracteres
        ------------------------------------
        Fase 2:
        
        Leer un XML desde un archivo almacenado en cualquier directorio
    """

    '''
    Llama al metodo xml_docto_base64_encoded() para pasarle por parametro una cadena de caracteres,
    en este caso, la cadena de caracteres a encodear a Base64 sera un XML de CFDI v.3.3 timbrado por el SAT
    '''

    # Prueba con XML version 3.2 del SAT ya timbrado:
    _xml_to_encode_str = """
                        <?xml version="1.0" encoding="utf-8"?><cfdi:Comprobante xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:detallista="http://www.sat.gob.mx/detallista" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd http://www.sat.gob.mx/detallista http://www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xsd" 
                            version="3.2" folio="60" fecha="2017-03-31T10:24:54" sello="FTOUrHPRuM+tKCKKBoPf6JfyKfXWMeaVhEcAaGQ/LynhoGmQhPxlz5BuFQOeJUbtnJMJvY55oazfXzSmmD7p/kLj98FVhNmwjZIq1KdUNgRUZEks/haXV/gKdn1ysJ1IXU3SVYk42BSmuREkOf17uaw1sChsUVet41krwNiCI7h45s38ZD7k0dx9kYI7alFla+ifFLW/kONTg1oodhEc6cwHFUwAT4AA2OSKdFr3qIEy63SBgf4iazgbzTNASIfgzYsOMlR5c/lqTTQ1K8GBC9F/I0gnTk0RxneljAkM5roHjkW7W1zfC63OZJPK+WZNpaETVqq+ofvtGG1d75wASA==" noCertificado="00001000000405087348" certificado="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" formaDePago="PAGO EN UNA SOLA EXHIBICION" subTotal="4173.71" descuento="0" Moneda="MXP" total="4841.50" tipoDeComprobante="ingreso" metodoDePago="03" LugarExpedicion="BLV. BELISARIO DOMINGUEZ NO. 1057 EDIFICIO B Y C, TUXTLA GUTIERREZ,CHIS.,MX., MEXICO"><cfdi:Emisor rfc="OFI920113KZ8" nombre="OFIX S.A. de C.V."><cfdi:DomicilioFiscal calle="AVENIDA URANO" noExterior="585" colonia="YLANG YLANG" localidad="BOCA DEL RIO" municipio="BOCA DEL RIO" estado="VERACRUZ" pais="MEXICO" codigoPostal="94298"/><cfdi:ExpedidoEn calle="BLV. BELISARIO DOMINGUEZ NO. 1057 EDIFICIO B Y C" localidad="TUXTLA GUTIERREZ,CHIS.,MX." pais="MEXICO"/><cfdi:RegimenFiscal Regimen="Regimen General de Ley Personas Morales"/></cfdi:Emisor><cfdi:Receptor rfc="CGI160330R94" nombre="CFE GENERACION IV"><cfdi:Domicilio calle="AV. PASEO DE LA REFORMA" noExterior="N&#176;. 164" colonia="JUAREZ" municipio="DELEGACION CUAHUTEMOC" localidad="MEXICO" estado="CIUDAD DE MEXICO" pais="MEXICO" codigoPostal="06600"/></cfdi:Receptor><cfdi:Conceptos><cfdi:Concepto cantidad="2" unidad="PIEZA" noIdentificacion="050-0002" descripcion="GRAPA STANDARD CON 5000PZAS PILOT 400" valorUnitario="21.98" importe="43.96"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="064-0004" descripcion="SUJETA DOCUMENTOS 32MM NEGRO C/12PZAS" valorUnitario="19.28" importe="57.84"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="064-0005" descripcion="SUJETA DOCUMENTOS 19MM NEGRO C/12PZAS" valorUnitario="10.29" importe="30.87"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="064-0010" descripcion="SUJETA DOCUMENTOS 51MM NEGRO C/12PZAS" valorUnitario="54.19" importe="162.57"/><cfdi:Concepto cantidad="3" unidad="CAJA 12" noIdentificacion="068-0162" descripcion="BOLIGRAFO MEDIANO STICK AZUL DIAMANTE BIC" valorUnitario="32.84" importe="98.52"/><cfdi:Concepto cantidad="6" unidad="PIEZA" noIdentificacion="070-0016" descripcion="CORRECTOR LIQUIDO TIPO PLUMA 8ML ZEBRA" valorUnitario="25.00" importe="150.00"/><cfdi:Concepto cantidad="2" unidad="PIEZA" noIdentificacion="075-0128" descripcion="LAPIZ BICOLOR HEXAG JUMBO SMART BOL CON 2" valorUnitario="8.94" importe="17.88"/><cfdi:Concepto cantidad="1" unidad="PIEZA" noIdentificacion="075-0386" descripcion="LAPIZ GRAFITO CON GOMA #2 TRIANGULAR MIRADO BLT CON 4" valorUnitario="15.38" importe="15.38"/><cfdi:Concepto cantidad="2" unidad="PIEZA" noIdentificacion="076-0406" descripcion="MARCADOR PERMANENTE DOBLE PUNTA SURTIDOS CON 3 SHARPIE" valorUnitario="44.20" importe="88.40"/><cfdi:Concepto cantidad="2" unidad="PIEZA" noIdentificacion="076-0610" descripcion="MARCADOR PERMANENTE FINO SURTIDOS CON 3 ELECTRO POP SHARPIE" valorUnitario="32.13" importe="64.26"/><cfdi:Concepto cantidad="5" unidad="PIEZA" noIdentificacion="087-0096" descripcion="NOTAS ADHESIVAS 3x4 NEON C/100H PAQUETE CON 6" valorUnitario="70.25" importe="351.25"/><cfdi:Concepto cantidad="5" unidad="PIEZA" noIdentificacion="087-0104" descripcion="NOTAS ADHESIVAS 3X3&#34; PASTEL C/6BLK MEMOTIP" valorUnitario="41.79" importe="208.95"/><cfdi:Concepto cantidad="10" unidad="PIEZA" noIdentificacion="087-0107" descripcion="NOTAS ADHESIVAS 2x2 CUBO ULTRA C/400H" valorUnitario="34.56" importe="345.60"/><cfdi:Concepto cantidad="1" unidad="PIEZA" noIdentificacion="092-0009" descripcion="CINTA EMPAQUE TRANSP TUK .48X50M" valorUnitario="10.80" importe="10.80"/><cfdi:Concepto cantidad="1" unidad="PIEZA" noIdentificacion="092-0012" descripcion="CINTA EMPAQUE CANELA TUK .48X50M" valorUnitario="10.80" importe="10.80"/><cfdi:Concepto cantidad="1" unidad="PIEZA" noIdentificacion="092-0057" descripcion="CINTA ADHESIVA TRANSP 205 .18X33M CELOFAN" valorUnitario="17.51" importe="17.51"/><cfdi:Concepto cantidad="2" unidad="PIEZA" noIdentificacion="093-0006" descripcion="CLIP MARIPOSA #2 CON 50" valorUnitario="25.21" importe="50.42"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="093-0012" descripcion="CLIP REDONDO #1 CON 100" valorUnitario="14.16" importe="42.48"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="093-0013" descripcion="CLIP REDONDO #2 CON 100" valorUnitario="10.89" importe="32.67"/><cfdi:Concepto cantidad="4" unidad="PIEZA" noIdentificacion="095-0279" descripcion="CUADERNO ESPIRAL FRANCES 100H RAYAS KIUT" valorUnitario="30.64" importe="122.56"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="095-0360" descripcion="CUADERNO PROFESIONAL 100H RAYAS NORMA COLOR" valorUnitario="39.19" importe="117.57"/><cfdi:Concepto cantidad="1" unidad="PIEZA 12" noIdentificacion="110-0034" descripcion="LAPIZ ADHESIVO 11GRS PRITT" valorUnitario="105.16" importe="105.16"/><cfdi:Concepto cantidad="6" unidad="PIEZA" noIdentificacion="110-0036" descripcion="LAPIZ ADHESIVO 22GRS PRITT" valorUnitario="17.44" importe="104.64"/><cfdi:Concepto cantidad="1" unidad="PIEZA" noIdentificacion="117-0033" descripcion="SOBRE BOLSA ANTE 60K COIN 5 CON 50" valorUnitario="15.58" importe="15.58"/><cfdi:Concepto cantidad="1" unidad="PIEZA" noIdentificacion="117-0037" descripcion="SOBRE BOLSA ANTE 88K CARTA CON 50" valorUnitario="72.10" importe="72.10"/><cfdi:Concepto cantidad="1" unidad="PIEZA" noIdentificacion="117-0038" descripcion="SOBRE BOLSA ANTE 88K OFICIO CON 50" valorUnitario="87.49" importe="87.49"/><cfdi:Concepto cantidad="10" unidad="PIEZA" noIdentificacion="117-0044" descripcion="SOBRE BOLSA ANTE 88K RADIOGRAFIA" valorUnitario="5.41" importe="54.10"/><cfdi:Concepto cantidad="2" unidad="PIEZA" noIdentificacion="248-0010" descripcion="PAPEL OPALINA CARTA BLANCA C/100HJS 120GRS" valorUnitario="38.50" importe="77.00"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="248-0088" descripcion="PAPEL CARTA PASTEL VERDE 37K C/100HJS" valorUnitario="31.02" importe="93.06"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="248-0091" descripcion="PAPEL CARTA PASTEL AMARILLO 37K C/100HJS" valorUnitario="31.02" importe="93.06"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="269-0182" descripcion="CARPETA ARGOLLA O 1.5&#34; CARTA BLANCO CON VENTANA" valorUnitario="38.96" importe="116.88"/><cfdi:Concepto cantidad="3" unidad="PIEZA" noIdentificacion="269-0260" descripcion="CARPETA ARGOLLA D 4&#34; CARTA NEGRO CON VENTANA" valorUnitario="88.64" importe="265.92"/><cfdi:Concepto cantidad="6" unidad="PIEZA" noIdentificacion="269-0302" descripcion="CARPETA OFIX ARGOLLA D 2&#34;  CARTA BLANCO CON VENTANA" valorUnitario="52.73" importe="316.38"/><cfdi:Concepto cantidad="5" unidad="PIEZA" noIdentificacion="285-0011" descripcion="SEPARADOR 15DIV COLORINDEX COLORES SURTIDOS" valorUnitario="43.35" importe="216.75"/><cfdi:Concepto cantidad="5" unidad="PIEZA" noIdentificacion="285-0015" descripcion="SEPARADOR 5DIV COLORINDEX COLORES SURTIDOS" valorUnitario="18.16" importe="90.80"/><cfdi:Concepto cantidad="5" unidad="PIEZA" noIdentificacion="285-0016" descripcion="SEPARADOR 8DIV COLORINDEX COLORES SURTIDOS" valorUnitario="22.45" importe="112.25"/><cfdi:Concepto cantidad="5" unidad="PIEZA" noIdentificacion="285-0072" descripcion="SEPARADOR 10DIV COLORINDEX COLORES SURTIDOS" valorUnitario="25.20" importe="126.00"/><cfdi:Concepto cantidad="5" unidad="PIEZA" noIdentificacion="285-0216" descripcion="MINIBANDERITAS FLECHA CON 96HJS COLORES BASICOS" valorUnitario="37.25" importe="186.25"/></cfdi:Conceptos><cfdi:Impuestos totalImpuestosTrasladados="667.79"><cfdi:Traslados><cfdi:Traslado tasa="16" impuesto="IVA" importe="667.79"/></cfdi:Traslados></cfdi:Impuestos><cfdi:Complemento><tfd:TimbreFiscalDigital xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" version="1.0" UUID="8E2C1724-EEA3-48C0-859E-69D96ABAF00D" FechaTimbrado="2017-03-31T11:45:23" selloCFD="FTOUrHPRuM+tKCKKBoPf6JfyKfXWMeaVhEcAaGQ/LynhoGmQhPxlz5BuFQOeJUbtnJMJvY55oazfXzSmmD7p/kLj98FVhNmwjZIq1KdUNgRUZEks/haXV/gKdn1ysJ1IXU3SVYk42BSmuREkOf17uaw1sChsUVet41krwNiCI7h45s38ZD7k0dx9kYI7alFla+ifFLW/kONTg1oodhEc6cwHFUwAT4AA2OSKdFr3qIEy63SBgf4iazgbzTNASIfgzYsOMlR5c/lqTTQ1K8GBC9F/I0gnTk0RxneljAkM5roHjkW7W1zfC63OZJPK+WZNpaETVqq+ofvtGG1d75wASA==" noCertificadoSAT="00001000000300250292" selloSAT="qcann7uVLSxSEAQBY2Q2XL1s45aJM86PsOQTsCwgC4x+vExaNEmtIIycbUYo/Yrb0ca9Sd4CrnLI7i3ekBjO0k7GVND7n7l6AZQu5C5AsTXo3I6GjiMjxVBXk7jHkYvgJmXCKubsikytkgxBY3AYN0Qu8G5Sj5QKNlVjJuBoUHQ=" xsi:schemaLocation="http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/TimbreFiscalDigital/TimbreFiscalDigital.xsd"/></cfdi:Complemento>
                        </cfdi:Comprobante>
                        """

    # Llama al metodo para encodear la cadena de caracteres que es un XML,
    # a su vez, se debe imprimir el resultado que es el XML encodeado

    xml_result_endoded = xml_docto_base64_encoded(_xml_to_encode_str)

    print("XML Encodeado desde Str: ", xml_result_endoded)

    # Prueba de encodeo a partir de un archivo XML almacenado en un directorio

    xml_byte_encode = read_xml_from_file_to_encode()

    print("XML Encodeado desde File: ", xml_byte_encode)


if __name__ == "__main__":

    main()

