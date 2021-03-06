#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 emijrp <emijrp@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import internetarchive

def main():
    #https://meta.wikimedia.org/wiki/List_of_Wikipedias
    langs = {
        "ab": "Abkhazian", 
        "ace": "Acehnese", 
        "ady": "Adyghe", 
        "af": "Afrikaans", 
        "ak": "Akan", 
        "am": "Amharic", 
        "an": "Aragonese", 
        "ang": "Anglo-Saxon", 
        "ar": "Arabic", 
        "arc": "Aramaic", 
        "arz": "Egyptian Arabic", 
        "as": "Assamese", 
        "ast": "Asturian", 
        "atj": "Atikamekw", 
        "av": "Avar", 
        "ay": "Aymara", 
        "az": "Azerbaijani", 
        "azb": "South Azerbaijani", 
        "ba": "Bashkir", 
        "bar": "Bavarian", 
        "bcl": "Central Bicolano", 
        "be": "Belarusian", 
        "bg": "Bulgarian", 
        "bi": "Bislama", 
        "bjn": "Banjar", 
        "bm": "Bambara", 
        "bn": "Bengali", 
        "bo": "Tibetan", 
        "bpy": "Bishnupriya Manipuri", 
        "br": "Breton", 
        "bs": "Bosnian", 
        "bug": "Buginese", 
        "bxr": "Buryat", 
        "ca": "Catalan", 
        "cdo": "Min Dong", 
        "ce": "Chechen", 
        "ceb": "Cebuano", 
        "ch": "Chamorro", 
        "cho": "Choctaw", 
        "chr": "Cherokee", 
        "chy": "Cheyenne", 
        "ckb": "Sorani", 
        "co": "Corsican", 
        "cr": "Cree", 
        "crh": "Crimean Tatar", 
        "cs": "Czech", 
        "csb": "Kashubian", 
        "cu": "Old Church Slavonic", 
        "cv": "Chuvash", 
        "cy": "Welsh", 
        "da": "Danish", 
        "de": "German", 
        "din": "Dinka", 
        "diq": "Zazaki", 
        "dsb": "Lower Sorbian", 
        "dty": "Doteli", 
        "dv": "Divehi", 
        "dz": "Dzongkha", 
        "ee": "Ewe", 
        "el": "Greek", 
        "eml": "Emilian-Romagnol", 
        "en": "English", 
        "eo": "Esperanto", 
        "es": "Spanish", 
        "et": "Estonian", 
        "eu": "Basque", 
        "ext": "Extremaduran", 
        "fa": "Persian", 
        "ff": "Fula", 
        "fi": "Finnish", 
        "fj": "Fijian", 
        "fo": "Faroese", 
        "fr": "French", 
        "frp": "Franco-Provençal", 
        "frr": "North Frisian", 
        "fur": "Friulian", 
        "fy": "West Frisian", 
        "ga": "Irish", 
        "gag": "Gagauz", 
        "gan": "Gan", 
        "gd": "Scottish Gaelic", 
        "gl": "Galician", 
        "glk": "Gilaki", 
        "gn": "Guarani", 
        "gom": "Goan Konkani", 
        "gor": "Gorontalo", 
        "got": "Gothic", 
        "gu": "Gujarati", 
        "gv": "Manx", 
        "ha": "Hausa", 
        "hak": "Hakka", 
        "haw": "Hawaiian", 
        "he": "Hebrew", 
        "hi": "Hindi", 
        "hif": "Fiji Hindi", 
        "ho": "Hiri Motu", 
        "hr": "Croatian", 
        "hsb": "Upper Sorbian", 
        "ht": "Haitian", 
        "hu": "Hungarian", 
        "hy": "Armenian", 
        "ia": "Interlingua", 
        "id": "Indonesian", 
        "ie": "Interlingue", 
        "ig": "Igbo", 
        "ik": "Inupiak", 
        "ilo": "Ilokano", 
        "inh": "Ingush", 
        "io": "Ido", 
        "is": "Icelandic", 
        "it": "Italian", 
        "iu": "Inuktitut", 
        "ja": "Japanese", 
        "jam": "Jamaican Patois", 
        "jbo": "Lojban", 
        "jv": "Javanese", 
        "ka": "Georgian", 
        "kaa": "Karakalpak", 
        "kab": "Kabyle", 
        "kbd": "Kabardian Circassian", 
        "kbp": "Kabiye", 
        "kg": "Kongo", 
        "ki": "Kikuyu", 
        "kj": "Kuanyama", 
        "kk": "Kazakh", 
        "kl": "Greenlandic", 
        "km": "Khmer", 
        "kn": "Kannada", 
        "ko": "Korean", 
        "koi": "Komi-Permyak", 
        "kr": "Kanuri", 
        "krc": "Karachay-Balkar", 
        "ks": "Kashmiri", 
        "ksh": "Ripuarian", 
        "ku": "Kurdish", 
        "kv": "Komi", 
        "kw": "Cornish", 
        "ky": "Kirghiz", 
        "la": "Latin", 
        "lad": "Ladino", 
        "lb": "Luxembourgish", 
        "lbe": "Lak", 
        "lez": "Lezgian", 
        "lfn": "Lingua Franca Nova", 
        "lg": "Luganda", 
        "li": "Limburgish", 
        "lij": "Ligurian", 
        "lmo": "Lombard", 
        "ln": "Lingala", 
        "lo": "Lao", 
        "lrc": "Northern Luri", 
        "lt": "Lithuanian", 
        "ltg": "Latgalian", 
        "lv": "Latvian", 
        "mai": "Maithili", 
        "mdf": "Moksha", 
        "mg": "Malagasy", 
        "mh": "Marshallese", 
        "mhr": "Meadow Mari", 
        "mi": "Maori", 
        "min": "Minangkabau", 
        "mk": "Macedonian", 
        "ml": "Malayalam", 
        "mn": "Mongolian", 
        "mr": "Marathi", 
        "mrj": "Hill Mari", 
        "ms": "Malay", 
        "mt": "Maltese", 
        "mus": "Muscogee", 
        "mwl": "Mirandese", 
        "my": "Burmese", 
        "myv": "Erzya", 
        "mzn": "Mazandarani", 
        "na": "Nauruan", 
        "nah": "Nahuatl", 
        "nap": "Neapolitan", 
        "nds": "Low Saxon", 
        "ne": "Nepali", 
        "new": "Newar", 
        "ng": "Ndonga", 
        "nl": "Dutch", 
        "nn": "Norwegian (Nynorsk)", 
        "no": "Norwegian (Bokmål)", 
        "nov": "Novial", 
        "nrm": "Norman", 
        "nso": "Northern Sotho", 
        "nv": "Navajo", 
        "ny": "Chichewa", 
        "oc": "Occitan", 
        "olo": "Livvi-Karelian", 
        "om": "Oromo", 
        "or": "Oriya", 
        "os": "Ossetian", 
        "pa": "Punjabi", 
        "pag": "Pangasinan", 
        "pam": "Kapampangan", 
        "pap": "Papiamentu", 
        "pcd": "Picard", 
        "pdc": "Pennsylvania German", 
        "pfl": "Palatinate German", 
        "pi": "Pali", 
        "pih": "Norfolk", 
        "pl": "Polish", 
        "pms": "Piedmontese", 
        "pnb": "Western Punjabi", 
        "pnt": "Pontic", 
        "ps": "Pashto", 
        "pt": "Portuguese", 
        "qu": "Quechua", 
        "rm": "Romansh", 
        "rmy": "Romani", 
        "rn": "Kirundi", 
        "ro": "Romanian", 
        "ru": "Russian", 
        "rue": "Rusyn", 
        "rw": "Kinyarwanda", 
        "sa": "Sanskrit", 
        "sah": "Sakha", 
        "sat": "Santali", 
        "sc": "Sardinian", 
        "scn": "Sicilian", 
        "sco": "Scots", 
        "sd": "Sindhi", 
        "se": "Northern Sami", 
        "sg": "Sango", 
        "sh": "Serbo-Croatian", 
        "shn": "Shan", 
        "si": "Sinhalese", 
        "sk": "Slovak", 
        "sl": "Slovenian", 
        "sm": "Samoan", 
        "sn": "Shona", 
        "so": "Somali", 
        "sq": "Albanian", 
        "sr": "Serbian", 
        "srn": "Sranan", 
        "ss": "Swati", 
        "st": "Sesotho", 
        "stq": "Saterland Frisian", 
        "su": "Sundanese", 
        "sv": "Swedish", 
        "sw": "Swahili", 
        "szl": "Silesian", 
        "ta": "Tamil", 
        "tcy": "Tulu", 
        "te": "Telugu", 
        "tet": "Tetum", 
        "tg": "Tajik", 
        "th": "Thai", 
        "ti": "Tigrinya", 
        "tk": "Turkmen", 
        "tl": "Tagalog", 
        "tn": "Tswana", 
        "to": "Tongan", 
        "tpi": "Tok Pisin", 
        "tr": "Turkish", 
        "ts": "Tsonga", 
        "tt": "Tatar", 
        "tum": "Tumbuka", 
        "tw": "Twi", 
        "ty": "Tahitian", 
        "tyv": "Tuvan", 
        "udm": "Udmurt", 
        "ug": "Uyghur", 
        "uk": "Ukrainian", 
        "ur": "Urdu", 
        "uz": "Uzbek", 
        "ve": "Venda", 
        "vec": "Venetian", 
        "vep": "Vepsian", 
        "vi": "Vietnamese", 
        "vls": "West Flemish", 
        "vo": "Volapük", 
        "wa": "Walloon", 
        "war": "Waray-Waray", 
        "wo": "Wolof", 
        "wuu": "Wu", 
        "xal": "Kalmyk", 
        "xh": "Xhosa", 
        "xmf": "Mingrelian", 
        "yi": "Yiddish", 
        "yo": "Yoruba", 
        "za": "Zhuang", 
        "zea": "Zeelandic", 
        "zh": "Chinese", 
        "zu": "Zulu", 
    }
    for langid, langword in langs.items():
        #https://archive.org/services/docs/api/internetarchive/quickstart.html#searching
        for i in internetarchive.search_items('subject:"kiwix" AND subject:"zim" AND subject:"%s"' % (langid)).iter_as_items():
            try:
                itemid = i.item_metadata['metadata']['identifier']
                print(itemid)
            except:
                print('Error in', i)
                continue
            if not 'language' in i.item_metadata['metadata']:
                if '_%s_' % (langid) in itemid:
                    r = internetarchive.modify_metadata(itemid, metadata=dict(language=langword))
                    if r.status_code == 200:
                        print('Language added: %s' % (langword))
                    else:
                        print('Error (%s) adding language: %s' % (r.status_code, langword))
                else:
                    print(i.item_metadata['metadata'])
                    print('Unknown language')
            else:
                print('Already has language: %s' % (i.item_metadata['metadata']['language']))

if __name__ == '__main__':
    main()
