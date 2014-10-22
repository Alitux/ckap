#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
#  ckap.py
#  
#  Copyright 2013 Alitux <alejandrofabrega@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import commands
import os
#Se verifica que existan los argumentos solicitados
try:
  NombreArchivo=sys.argv[1]
  CabeceraCalibracion=sys.argv[2]
except IndexError:
  if NombreArchivo.lower()=="help":
    print """
    ckap V0.1 2014
    --------------
    
    Uso: Crea una carta raster a partir de una imagen y un archivo de calibración .dir
    (generado con MapCalParte de la suite SeaClearII, por ejemplo)
    
    Sintaxis: ckap [imagen] [Cabecera.dir]
    
    """
    sys.exit()
  else:
    print "Se requieren dos argumentos: ckap [imagen] [Cabecera.dir]"
    sys.exit()
try:
  CabeceraCalibracion=sys.argv[2]
except IndexError:
    print "Se requieren dos argumentos: ckap [imagen] [Cabecera.dir]"
    sys.exit()

if NombreArchivo.lower()=="help":
    print "Sintaxis: ckap \"[imagen]\" \"[Cabecera.dir]\""
    print "Importante: NO OLVIDAR COMILLAS EN LOS ARGUMENTOS"
    
#Rutas Absolutas de los archivos
AbsRutaArchivo="\""+os.getcwd()+"/"+NombreArchivo+"\""
AbsRutaCabecera="\""+os.getcwd()+"/"+CabeceraCalibracion+"\""
#print AbsRutaArchivo #Descomentar para debug
#print AbsRutaCabecera #Descomentar para debug
#1- Conversión de Cabecera a .hdr
ConversionCabecera=commands.getoutput("mc2bsbh "+AbsRutaCabecera+" -o hdrtmp.hdr")

#2- Conversion de imagen a tif
print "Unión en proceso. Por favor espere..."
ConversionCabeceragif=commands.getoutput("convert "+AbsRutaArchivo+" -colors 127 "+AbsRutaArchivo+".gif")
ConversionCabeceratif=commands.getoutput("convert "+AbsRutaArchivo+".gif -colors 127 "+AbsRutaArchivo+".tif")
#print ConversionCabeceragif #Descomentar para debug
#print ConversionCabeceratif #Descomentar para debug

#3- Union de cabecera con imagen tif
NombreCarta="\""+os.getcwd()+"/"+os.path.splitext(NombreArchivo)[0]+".kap"
union=commands.getoutput("tif2bsb -c 127 hdrtmp.hdr "+"\""+os.getcwd()+"/"+NombreArchivo+".tif\" "+ "\""+os.path.splitext(NombreArchivo)[0]+".kap\"")
print "¡Se creó exitosamente la carta!"
#print union #Descomentar para debug

#4- Borrar archivos temporales
borrar=commands.getoutput("rm "+AbsRutaArchivo+".gif "+AbsRutaArchivo+".tif hdrtmp.hdr")
print borrar #Descomentar para debug