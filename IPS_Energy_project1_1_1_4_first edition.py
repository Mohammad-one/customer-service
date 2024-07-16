import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import floor
from cx_Freeze import setup, Executable
from tkinter import filedialog


# Define the inverter dictionary (same as in your code)
inverters = {
    'SUN2000-3KTL-M1': {
        'Output Power': '3000Wp',
        'Max. output current': '5.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-4KTL-M1': {
        'Output Power': '4000Wp',
        'Max. output current': '6.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-5KTL-M1': {
        'Output Power': '5000Wp',
        'Max. output current': '8.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-6KTL-M1': {
        'Output Power': '6000Wp',
        'Max. output current': '10.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-8KTL-M1': {
        'Output Power': '8000Wp',
        'Max. output current': '13.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-10KTL-M1': {
        'Output Power': '10000Wp',
        'Max. output current': '16.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    #---
    'SUN2000-12KTL-M5': {
        'Output Power': '12000Wp',
        'Max. output current': '17.3A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-15KTL-M5': {
        'Output Power': '15000Wp',
        'Max. output current': '23.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-17KTL-M5': {
        'Output Power': '17000Wp',
        'Max. output current': '27.1A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-20KTL-M5': {
        'Output Power': '20000Wp',
        'Max. output current': '31.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-25KTL-M5': {
        'Output Power': '25000Wp',
        'Max. output current': '39.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    #---------------
    'SUN2000-2KTL-L1': {
        'Output Power': '2000Wp',
        'Max. output current': '10A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-3KTL-L1': {
        'Output Power': '3000Wp',
        'Max. output current': '15A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-3.68KTL-L1': {
        'Output Power': '3680Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-4KTL-L1': {
        'Output Power': '4000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-4.6KTL-L1': {
        'Output Power': '4600Wp',
        'Max. output current': '23A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-5KTL-L1': {
        'Output Power': '5000Wp',
        'Max. output current': '25A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-6KTL-L1': {
        'Output Power': '6000Wp',
        'Max. output current': '27.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    #-------------------------------
    'NAC4K-DS': {
        'Output Power': '4000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    'NAC5K-DS': {
        'Output Power': '5000Wp',
        'Max. output current': '25A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    'NAC6K-DS': {
        'Output Power': '6000Wp',
        'Max. output current': '27.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    #-------
    'R1-1K1-SS': {
        'Output Power': '1000Wp',
        'Max. output current': '5A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-1K6-SS': {
        'Output Power': '1000Wp',
        'Max. output current': '7.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-2K2-SS': {
        'Output Power': '2000Wp',
        'Max. output current': '9.6A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-2K7-SS': {
        'Output Power': '2000Wp',
        'Max. output current': '12.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-3K3-SS': {
        'Output Power': '3000Wp',
        'Max. output current': '15A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-3K7-SS': {
        'Output Power': '3000Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    #------------------------
    'R3-4K-DT': {
        'Output Power': '4000Wp',
        'Max. output current': '6.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-5K-DT': {
        'Output Power': '5000Wp',
        'Max. output current': '8.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-6K-DT': {
        'Output Power': '6000Wp',
        'Max. output current': '10A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-8K-DT': {
        'Output Power': '8000Wp',
        'Max. output current': '13.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-10K-DT': {
        'Output Power': '10000Wp',
        'Max. output current': '16.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-12K-DT': {
        'Output Power': '12000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-15K-DT': {
        'Output Power': '15000Wp',
        'Max. output current': '22.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    #---------------------------
    'R3-30K-G5': {
        'Output Power': '30000Wp',
        'Max. output current': '47.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-33K-G5': {
        'Output Power': '33000Wp',
        'Max. output current': '52.6A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-36K-G5': {
        'Output Power': '36000Wp',
        'Max. output current': '57.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-40K-G5': {
        'Output Power': '40000Wp',
        'Max. output current': '63.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    #---------------------
    'SUN2000-30KTL-M3': {
        'Output Power': '30000Wp',
        'Max. output current': '47.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-36KTL-M3': {
        'Output Power': '36000Wp',
        'Max. output current': '58.0A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-40KTL-M3': {
        'Output Power': '40000Wp',
        'Max. output current': '63.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    #-------------------------------------------------------------------------
    'S5-GR3P-3K': {
        'Output Power': '3000Wp',
        'Max. output current': '4.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-4K': {
        'Output Power': '4000Wp',
        'Max. output current': '6.4A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-5K': {
        'Output Power': '5000Wp',
        'Max. output current': '7.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-6K': {
        'Output Power': '6000Wp',
        'Max. output current': '9.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-8K': {
        'Output Power': '8000Wp',
        'Max. output current': '12.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-9K': {
        'Output Power': '9000Wp',
        'Max. output current': '14.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-10K': {
        'Output Power': '10000Wp',
        'Max. output current': '15.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-12K': {
        'Output Power': '12000Wp',
        'Max. output current': '19.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-13K': {
        'Output Power': '13000Wp',
        'Max. output current': '20.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-15K': {
        'Output Power': '15000Wp',
        'Max. output current': '23.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-17K': {
        'Output Power': '17000Wp',
        'Max. output current': '27A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    'S5-GR3P-20K': {
        'Output Power': '20000Wp',
        'Max. output current': '31.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-1000'
    },
    #===========================================================================
    'S5-GC50K':{
        'Output Power': '50000Wp',
        'Max. output current': '83.6A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    'S5-GC60K':{
        'Output Power': '60000Wp',
        'Max. output current': '100.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    #==========================================================================
    '1PH-3k-TLM-V3':{
        'Output Power': '3000Wp',
        'Max. output current': '13.6A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '200-500'
    },
    '1PH-3.68k-TLM-V3':{
        'Output Power': '3600Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '200-500'
    },
    '1PH-4k-TLM-V3':{
        'Output Power': '4000Wp',
        'Max. output current': '18.2A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '200-500'
    },
    '1PH-4.6k-TLM-V3':{
        'Output Power': '4600Wp',
        'Max. output current': '21A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '200-500'
    },
    #============+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '3PH-3.3KTL-V1':{
        'Output Power': '3300Wp',
        'Max. output current': '4.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-960'
    },
    '3PH-4.4KTL-V1':{
        'Output Power': '4400Wp',
        'Max. output current': '6.4A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-960'
    },
    '3PH-5.5KTL-V1':{
        'Output Power': '5500Wp',
        'Max. output current': '8.0A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-960'
    },
    '3PH-6.6KTL-V1':{
        'Output Power': '6600Wp',
        'Max. output current': '9.6A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-960'
    },
    '3PH-8.8KTL-V1':{
        'Output Power': '8800Wp',
        'Max. output current': '12.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-960'
    },
    '3PH-11KTL-V1':{
        'Output Power': '11000Wp',
        'Max. output current': '15.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-960'
    },
    '3PH-12KTL-V1':{
        'Output Power': '12000Wp',
        'Max. output current': '19.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '160-960'
    },
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=
    'Sunny Tripower-10KTL': {
        'Output Power': '10000Wp',
        'Max. output current': '16A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '320-800'
    },
    'Sunny Tripower-12KTL': {
        'Output Power': '12000Wp',
        'Max. output current': '19.2A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '380-800'
    },
    'Sunny Tripower-15KTL': {
        'Output Power': '15000Wp',
        'Max. output current': '24A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '360-800'
    },
    'Sunny Tripower-17KTL': {
        'Output Power': '17000Wp',
        'Max. output current': '24.6A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '400-800'
    },
    #----------------------------------------------------------
    'Sunny Mini Central-4.6KA': {
        'Output Power': '4600Wp',
        'Max. output current': '26A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '246-480'
    },
    'Sunny Mini Central-5KA': {
        'Output Power': '5000Wp',
        'Max. output current': '26A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '246-480'
    },
    'Sunny Mini Central-6KA': {
        'Output Power': '6000Wp',
        'Max. output current': '26A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '246-480'
    },
    'Sunny Boy 2100TL': {
        'Output Power': '2100Wp',
        'Max. output current': '11A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '200-480'
    },
    #============================================================
    'S6-GR1P-0.6K-M': {
        'Output Power': '600Wp',
        'Max. output current': '2.6A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'S6-GR1P-0.7K-M': {
        'Output Power': '700Wp',
        'Max. output current': '4.4A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'S6-GR1P-1K-M': {
        'Output Power': '1000Wp',
        'Max. output current': '5.2A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'S6-GR1P-1.5K-M': {
        'Output Power': '1500Wp',
        'Max. output current': '8.1A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'S6-GR1P-2K-M': {
        'Output Power': '2000Wp',
        'Max. output current': '10.5A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-500'
    },
    'S6-GR1P-2.5K-M': {
        'Output Power': '2500Wp',
        'Max. output current': '13.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-500'
    },
    'S6-GR1P-3K-M': {
        'Output Power': '3000Wp',
        'Max. output current': '15.7A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-500'
    },
    'S6-GR1P-3.6K-M': {
        'Output Power': '3600Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-500'
    },
    #===============================================================================
    '3PH-3.3KTL-V3': {
        'Output Power': '3300Wp',
        'Max. output current': '5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    '3PH-4.4KTL-V3': {
        'Output Power': '4400Wp',
        'Max. output current': '6.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    '3PH-5.5KTL-V3': {
        'Output Power': '5500Wp',
        'Max. output current': '8.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    '3PH-6.6KTL-V3': {
        'Output Power': '6600Wp',
        'Max. output current': '10A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    '3PH-8.8KTL-V3': {
        'Output Power': '8800Wp',
        'Max. output current': '13.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    '3PH-11KTL-V3': {
        'Output Power': '11000Wp',
        'Max. output current': '16.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    '3PH-12KTL-V3': {
        'Output Power': '12000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    '3PH-25KTL-V3' : {
        'Output Power': '25000Wp',
        'Max. output current': '42.4A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    '3PH-30KTL-V3' : {
        'Output Power': '30000Wp',
        'Max. output current': '51.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    '3PH-33KTL-V3' : {
        'Output Power': '33000Wp',
        'Max. output current': '56A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    '3PH-36KTL-V3' : {
        'Output Power': '36000Wp',
        'Max. output current': '60.6A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    '3PH-40KTL-V3' : {
        'Output Power': '40000Wp',
        'Max. output current': '66.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    '3PH-45KTL-V3' : {
        'Output Power': '45000Wp',
        'Max. output current': '75.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    '3PH-50KTL-V3' : {
        'Output Power': '50000Wp',
        'Max. output current': '83.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '180-1000'
    },
    #================================================================
    'BluE-8KT-M1':{
        'Output Power': '8000Wp',
        'Max. output current': '12.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    'BluE-10KT-M1':{
        'Output Power': '10000Wp',
        'Max. output current': '16A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    'BluE-12KT-M1':{
        'Output Power': '12000Wp',
        'Max. output current': '19.2A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'   
    },
    'BluE-15KT-M1':{
        'Output Power': '15000Wp',
        'Max. output current': '23.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    'BluE-17KT-M1':{
        'Output Power': '17000Wp',
        'Max. output current': '27.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    'BluE-20KT-M1':{
        'Output Power': '20000Wp',
        'Max. output current': '31.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    'BluE-22KT-M1':{
        'Output Power': '22000Wp',
        'Max. output current': '35.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    'BluE-23KT-M1':{
        'Output Power': '23000Wp',
        'Max. output current': '36.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    'BluE-25KT-M1':{
        'Output Power': '25000Wp',
        'Max. output current': '39.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-1000'
    },
    #++++++++++++++++++++++++++++++++++++++++++++++
    'Sunny Tripower- 15000TL' :{
        'Output Power': '15000Wp',
        'Max. output current': '29A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '240-600'
    },
    'Sunny Tripower- 20000TL' :{
        'Output Power': '20000Wp',
        'Max. output current': '29A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '320-600'
    },
    'Sunny Tripower- 25000TL' :{
        'Output Power': '25000Wp',
        'Max. output current': '36.2A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '390-600'
    },
    #++++++++++++++++++++++++++++++++++++++++
    'Sunny-Tripower-8k' : {
        'Output Power': '8000Wp',
        'Max. output current': '30A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '260-800'
    },
    'Sunny-Tripower-10k' : {
        'Output Power': '10000Wp',
        'Max. output current': '30A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '320-800'
    },
    #++++++++++++++++++++++++++++++++++++++++
    'Sunny-Boy-3k' : {
        'Output Power': '3000Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '110-500'
    },
    'Sunny-Boy-3.6k' : {
        'Output Power': '3600Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '130-500'
    },
    'Sunny-Boy-4k' : {
        'Output Power': '4000Wp',
        'Max. output current': '22A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '140-500'
    },
    'Sunny-Boy-5k' : {
        'Output Power': '5000Wp',
        'Max. output current': '22A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '175-500'
    },
    #++++++++++++++++++++++++++++++++++++++++
    '3000S-M1' : {
        'Output Power': '3000Wp',
        'Max. output current': '14.4A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-560'
    },
    '3000D-M1' : {
        'Output Power': '3000Wp',
        'Max. output current': '14.4A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-560'
    },
    '4000D-M1' : {
        'Output Power': '4000Wp',
        'Max. output current': '19A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-560'
    },
    '5000D-M1' : {
        'Output Power': '5000Wp',
        'Max. output current': '24A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-560'
    },
    '6000D-M1' : {
        'Output Power': '6000Wp',
        'Max. output current': '26A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '80-560'
    },
}


# Function to calculate and display suitable inverters
def calculate_inverters():
    try:
        client_name = entry_client_name.get().strip()
        conso = int(entry_consumption.get())
        p1 = conso / 1600
        
        # Determine the number of panels and final power
        if p1 > 4.2:
            number_panels = floor(p1 / 0.590)
            p_f = number_panels * 590
            panel_wattage = 590
        else:
            number_panels = floor(p1 / 0.420)
            p_f = number_panels * 420
            panel_wattage = 420

        # Get the client current counter value
        client_current_counter = float(entry_client_current_counter.get())

        suitable_inverters = []
        for inverter, specs in inverters.items():
            max_power = int(specs['Output Power'].replace('Wp', ''))
            max_output_current = float(specs['Max. output current'].replace('A', '').split('/')[0])  # Handle cases with "A/400Vac"
            ratio = p_f / max_power
            
            if 0.9 < ratio < 1.3:
                if panel_wattage == 590 and 13.9 < max_output_current < client_current_counter:
                    suitable_inverters.append((inverter, specs))
                elif panel_wattage == 420 and 10.01 < max_output_current < client_current_counter:
                    suitable_inverters.append((inverter, specs))
        
        results_text.config(state=tk.NORMAL)
        results_text.delete('1.0', tk.END)
        results_text.insert(tk.END, f"Client's Name: {client_name}\n")
        results_text.insert(tk.END, f"Number of panels required: {number_panels}\n")
        results_text.insert(tk.END, f"You have to use {panel_wattage}W panel.\n")
        results_text.insert(tk.END, f"Total power from panels: {p_f}W\n\n")

        if suitable_inverters:
            results_text.insert(tk.END, "Suitable Inverters:\n")
            results_text.insert(tk.END, "-------------------\n")
            for inverter, specs in suitable_inverters:
                results_text.insert(tk.END, f"Inverter Model: {inverter}\n")
                for key, value in specs.items():
                    results_text.insert(tk.END, f"  {key}: {value}\n")
                results_text.insert(tk.END, "\n")
        else:
            results_text.insert(tk.END, "No suitable inverters found.\n")
        
        results_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for consumption and client current counter.")

# Function to save results to a file
def save_results():
    try:
        client_name = entry_client_name.get().strip()
        filename = filedialog.asksaveasfilename(
            defaultextension='.txt', 
            filetypes=[('Text files', '*.txt'), ('All files', '*.*')],
            initialfile=f"{client_name}_results.txt" if client_name else "results.txt"
        )
        if filename:
            with open(filename, 'w') as f:
                f.write(results_text.get('1.0', tk.END))
            messagebox.showinfo("Success", "Results saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save results: {e}")

# Create main window
root = tk.Tk()
root.title("Solar Inverter Selector")

# Colors for improved user interface
primary_color = '#4CAF50'  # Green
secondary_color = '#008CBA'  # Blue
accent_color = '#f44336'  # Red
background_color = '#E0F7FA'  # Light Blue                                      

# Create and place widgets with improved styling
main_frame = tk.Frame(root, padx=20, pady=20, bg=background_color)  # Light blue background
main_frame.pack(fill=tk.BOTH, expand=True)

# Header label
header_label = tk.Label(main_frame, text="Solar Inverter Selector", font=("Arial", 20), bg=background_color)  # Light blue background
header_label.pack(pady=(0, 20))

# Client name input
client_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
client_frame.pack()

label_client_name = tk.Label(client_frame, text="Client Name:", font=("Arial", 12), bg=background_color)
label_client_name.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

entry_client_name = tk.Entry(client_frame, width=30, font=("Arial", 12))
entry_client_name.grid(row=0, column=1, padx=10, pady=10)

# Client current counter input
label_client_current_counter = tk.Label(client_frame, text="Client Current Counter:", font=("Arial", 12), bg=background_color)
label_client_current_counter.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

entry_client_current_counter = tk.Entry(client_frame, width=10, font=("Arial", 12))
entry_client_current_counter.grid(row=1, column=1, padx=10, pady=10)

# Input frame
input_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
input_frame.pack()

label_consumption = tk.Label(input_frame, text="Enter your consumption in W:", font=("Arial", 12), bg=background_color)  # Light blue background
label_consumption.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

entry_consumption = tk.Entry(input_frame, width=10, font=("Arial", 12))
entry_consumption.grid(row=0, column=1, padx=10, pady=10)

# Results display
results_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
results_frame.pack(fill=tk.BOTH, expand=True, pady=20)

results_text = tk.Text(results_frame, wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED, bg='#FFFFFF')  # White background
results_text.pack(fill=tk.BOTH, expand=True)

# Buttons
button_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate", font=("Arial", 12), bg=primary_color, fg='#FFFFFF', command=calculate_inverters)
calculate_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(button_frame, text="Save Results", font=("Arial", 12), bg=secondary_color, fg='#FFFFFF', command=save_results)
save_button.pack(side=tk.LEFT, padx=10)

# Exit button
exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), bg=accent_color, fg='#FFFFFF', command=root.quit)
exit_button.pack(side=tk.LEFT, padx=10)


size = len(inverters)
print(f"The Number of the Inverters is: {size}")




# Start the main loop
root.mainloop()
