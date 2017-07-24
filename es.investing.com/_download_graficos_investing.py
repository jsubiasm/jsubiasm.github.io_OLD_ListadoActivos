import urllib2

urls = ([
	"http://es.investing.com/indices/eu-stoxx50-chart?cid=40828",
	"http://es.investing.com/indices/germany-30-chart?cid=23657",
	"http://es.investing.com/indices/uk-100-chart?cid=27517",
	"http://es.investing.com/indices/switzerland-20-chart?cid=40829",
	"http://es.investing.com/indices/netherlands-25-chart?cid=23659",
	"http://es.investing.com/indices/france-40-chart?cid=23658",
	"http://es.investing.com/indices/bel-20-chart?cid=954865",
	"http://es.investing.com/indices/omx-stockholm-30-chart",
	"http://es.investing.com/indices/it-mib-40-chart?cid=27309",
	"http://es.investing.com/indices/psi-20-chart?cid=954863",
	"http://es.investing.com/indices/spain-35-chart?cid=26491",
	"http://es.investing.com/indices/us-spx-500-chart?cid=40826",
	"http://es.investing.com/indices/us-30-chart",
	"http://es.investing.com/indices/nasdaq-composite-chart",
	"http://es.investing.com/indices/s-p-tsx-composite-chart",
	"http://es.investing.com/indices/ipsa-chart",
	"http://es.investing.com/indices/bovespa-chart",
	"http://es.investing.com/indices/merv-chart",
	"http://es.investing.com/indices/colcap-chart",
	"http://es.investing.com/indices/lima-stock-exchange-general-chart",
	"http://es.investing.com/indices/ipc-chart",
	"http://es.investing.com/indices/mcx-chart",
	"http://es.investing.com/indices/rtsi-chart",
	"http://es.investing.com/indices/japan-ni225-chart",
	"http://es.investing.com/indices/ftse-china-a50-chart",
	"http://es.investing.com/indices/hang-sen-40-chart?cid=38011",
	"http://es.investing.com/indices/taiwan-weighted-chart",
	"http://es.investing.com/indices/kospi-chart",
	"http://es.investing.com/indices/idx-composite-chart",
	"http://es.investing.com/indices/s-p-cnx-nifty-chart",
	"http://es.investing.com/indices/sensex-chart",
	"http://es.investing.com/indices/cse-all-share-chart",
	"http://es.investing.com/etfs/spdr-consumer-discr.-select-sector-chart",
	"http://es.investing.com/etfs/spdr---consumer-staples-chart",
	"http://es.investing.com/etfs/spdr-energy-select-sector-fund-chart",
	"http://es.investing.com/etfs/financial-select-sector-spdr-fund-chart",
	"http://es.investing.com/etfs/financial-services-select-sector-chart",
	"http://es.investing.com/etfs/spdr---health-care-chart",
	"http://es.investing.com/etfs/industrial-sector-spdr-trust-chart",
	"http://es.investing.com/etfs/spdr-materials-select-sector-etf-chart",
	"http://es.investing.com/etfs/spdr-select-sector---technology-chart",
	"http://es.investing.com/etfs/spdr-select-sector---utilities-chart",
	"http://es.investing.com/etfs/ishares-djsu-broker-dealers-index-chart",
	"http://es.investing.com/etfs/spdr-kbw-capital-markets-chart",
	"http://es.investing.com/etfs/ishares-djsu-financial-services-chart",
	"http://es.investing.com/etfs/ishares-djsu-financial-sector-chart",
	"http://es.investing.com/etfs/spdr-kbw-bank-chart",
	"http://es.investing.com/etfs/spdr-kbw-regional-banking-chart",
	"http://es.investing.com/etfs/spdr-kbw-insurance-chart",
	"http://es.investing.com/etfs/ishares-djsu-medical-devices-index-chart",
	"http://es.investing.com/etfs/ishares-djsu-health-care-providers-chart",
	"http://es.investing.com/etfs/ishares-djsu-health-care-index-chart",
	"http://es.investing.com/etfs/spdr-s-p-pharmaceuticals-chart",
	"http://es.investing.com/etfs/spdr-s-p-biotech-chart",
	"http://es.investing.com/etfs/ishares-djsu-technology-chart",
	"http://es.investing.com/etfs/ishares-djsu-telecommunications-chart",
	"http://es.investing.com/etfs/spdr-s-p-semiconductor-chart",
	"http://es.investing.com/etfs/spdr-s-p-software---services-chart",
	"http://es.investing.com/etfs/ishares-djsu-aerospace---defense-chart",
	"http://es.investing.com/etfs/ishares-djsu-basic-materials-index-chart",
	"http://es.investing.com/etfs/spdr-s-p-metals---mining-chart",
	"http://es.investing.com/etfs/spdr-s-p-transportation-chart",
	"http://es.investing.com/etfs/ishares-djsu-industrial-sector-chart",
	"http://es.investing.com/etfs/ishares-djsu-utilities-chart",
	"http://es.investing.com/etfs/ishares-dj-us-energy-sector-fund-chart",
	"http://es.investing.com/etfs/spdr-s-p-oil--gas-explor---product-chart",
	"http://es.investing.com/etfs/spdr-s-p-oil---gas-eq---services-chart",
	"http://es.investing.com/etfs/spdr-s-p-homebuilders-chart",
	"http://es.investing.com/etfs/spdr-s-p-retail-chart",
	"http://es.investing.com/etfs/ishares-djsu-consumer-goods-index-chart",
	"http://es.investing.com/etfs/ishares-djsu-consumer-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-auto-parts-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-banks-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-basicresources-chart",
	"http://es.investing.com/etfs/ishares-stoxx-europe-600-chemicals-chart",
	"http://es.investing.com/etfs/ishares-stoxxeuro-600-cons.---mat.-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-financial-svs-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-food-beverage-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-health-care-chart",
	"http://es.investing.com/etfs/ishares-stoxx600-ind.-goods--ser.-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-insurance-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-media-chart",
	"http://es.investing.com/etfs/ishares-dj-stoxx600-oil-gas-chart",
	"http://es.investing.com/etfs/ishares-stoxx-600-pers-housld-gds-chart",
	"http://es.investing.com/etfs/ishares-eurostoxx-600-real-estate-chart",
	"http://es.investing.com/etfs/ishares-stoxx-euro-600-retail-chart",
	"http://es.investing.com/etfs/ishares-eurostoxx-600-technology-chart",
	"http://es.investing.com/etfs/ishares-eurostoxx-600-telecom--de-chart",
	"http://es.investing.com/etfs/ishares-eurostoxx600-trvl---leis.-chart",
	"http://es.investing.com/etfs/ishares-eurostoxx-600-utilities-chart",
	"https://es.investing.com/commodities/gold-streaming-chart",
	"http://es.investing.com/commodities/silver-streaming-chart",
	"http://es.investing.com/commodities/crude-oil-streaming-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-eur-gbp",
	"https://es.investing.com/currencies/gr%C3%A1fico-eur-chf",
	"https://es.investing.com/currencies/gr%C3%A1fico-eur-usd",
	"https://es.investing.com/currencies/gr%C3%A1fico-eur-cad",
	"https://es.investing.com/currencies/gr%C3%A1fico-eur-aud",
	"https://es.investing.com/currencies/gr%C3%A1fico-eur-nzd",
	"https://es.investing.com/currencies/gr%C3%A1fico-eur-jpy",
	"https://es.investing.com/currencies/gbp-eur-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-gbp-chf",
	"https://es.investing.com/currencies/gr%C3%A1fico-gbp-usd",
	"https://es.investing.com/currencies/gr%C3%A1fico-gbp-cad",
	"https://es.investing.com/currencies/gr%C3%A1fico-gbp-aud",
	"https://es.investing.com/currencies/gr%C3%A1fico-gbp-nzd",
	"https://es.investing.com/currencies/gr%C3%A1fico-gbp-jpy",
	"https://es.investing.com/currencies/chf-eur-chart",
	"https://es.investing.com/currencies/chf-gbp-chart",
	"https://es.investing.com/currencies/chf-usd-chart",
	"https://es.investing.com/currencies/chf-cad-chart",
	"https://es.investing.com/currencies/chf-aud-chart",
	"https://es.investing.com/currencies/chf-nzd-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-chf-jpy",
	"https://es.investing.com/currencies/usd-eur-chart",
	"https://es.investing.com/currencies/usd-gbp-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-usd-chf",
	"https://es.investing.com/currencies/gr%C3%A1fico-usd-cad",
	"https://es.investing.com/currencies/usd-aud-chart",
	"https://es.investing.com/currencies/usd-nzd-chart",
	"https://es.investing.com/currencies/cad-eur-chart",
	"https://es.investing.com/currencies/cad-gbp-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-cad-chf",
	"https://es.investing.com/currencies/cad-usd-chart",
	"https://es.investing.com/currencies/cad-aud-chart",
	"https://es.investing.com/currencies/cad-nzd-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-cad-jpy",
	"https://es.investing.com/currencies/aud-eur-chart",
	"https://es.investing.com/currencies/aud-gbp-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-aud-chf",
	"https://es.investing.com/currencies/gr%C3%A1fico-aud-usd",
	"https://es.investing.com/currencies/gr%C3%A1fico-aud-cad",
	"https://es.investing.com/currencies/gr%C3%A1fico-aud-nzd",
	"https://es.investing.com/currencies/gr%C3%A1fico-aud-jpy",
	"https://es.investing.com/currencies/nzd-eur-chart",
	"https://es.investing.com/currencies/nzd-gbp-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-nzd-chf",
	"https://es.investing.com/currencies/gr%C3%A1fico-nzd-usd",
	"https://es.investing.com/currencies/gr%C3%A1fico-nzd-cad",
	"https://es.investing.com/currencies/nzd-aud-chart",
	"https://es.investing.com/currencies/gr%C3%A1fico-nzd-jpy",
	"https://es.investing.com/currencies/jpy-eur-chart",
	"https://es.investing.com/currencies/jpy-gbp-chart",
	"https://es.investing.com/currencies/jpy-chf-chart",
	"https://es.investing.com/currencies/jpy-usd-chart",
	"https://es.investing.com/currencies/jpy-cad-chart",
	"https://es.investing.com/currencies/jpy-aud-chart",
	"https://es.investing.com/currencies/jpy-nzd-chart"
])

for i in range(len(urls)):
	url = urls[i]
	print url
	req = urllib2.Request(url)
	req.add_header("User-Agent", "Mozilla/5.0")
	f = urllib2.urlopen(req)
	data = f.read()
	with open("file" + `i` + ".html", "wb") as code:
		code.write(data)
