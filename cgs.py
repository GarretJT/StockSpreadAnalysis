import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import time

# Streamlit App Title
st.title("Stock Spread Analysis")

# Tickers List (example, you can add your full list of tickers)
tickers = [
    "AALI.JK", "ABBA.JK", "ABDA.JK", "ABMM.JK", "ACES.JK", "ACST.JK", "ADES.JK", "ADHI.JK", "ADMF.JK", "ADMG.JK", "ADRO.JK", "AGII.JK", "AGRO.JK", "AGRS.JK", "AHAP.JK", "AIMS.JK", "AISA.JK", "AKKU.JK", "AKPI.JK", "AKRA.JK", "AKSI.JK", "ALDO.JK", "ALKA.JK", "ALMI.JK", "ALTO.JK", "AMAG.JK", "AMFG.JK", "AMIN.JK", "AMRT.JK", "ANJT.JK", "ANTM.JK", "APEX.JK", "APIC.JK", "APII.JK", "APLI.JK", "APLN.JK", "ARGO.JK", "ARII.JK", "ARNA.JK", "ARTA.JK", "ARTI.JK", "ARTO.JK", "ASBI.JK", "ASDM.JK", "ASGR.JK", "ASII.JK", "ASJT.JK", "ASMI.JK", "ASRI.JK", "ASRM.JK", "ASSA.JK", "ATIC.JK", "AUTO.JK", "BABP.JK", "BACA.JK", "BAJA.JK", "BALI.JK", "BAPA.JK", "BATA.JK", "BAYU.JK", "BBCA.JK", "BBHI.JK", "BBKP.JK", "BBLD.JK", "BBMD.JK", "BBNI.JK", "BBRI.JK", "BBRM.JK", "BBTN.JK", "BBYB.JK", "BCAP.JK", "BCIC.JK", "BCIP.JK", "BDMN.JK", "BEKS.JK", "BEST.JK", "BFIN.JK", "BGTG.JK", "BHIT.JK", "BIKA.JK", "BIMA.JK", "BINA.JK", "BIPI.JK", "BIPP.JK", "BIRD.JK", "BISI.JK", "BJBR.JK", "BJTM.JK", "BKDP.JK", "BKSL.JK", "BKSW.JK", "BLTA.JK", "BLTZ.JK", "BMAS.JK", "BMRI.JK", "BMSR.JK", "BMTR.JK", "BNBA.JK", "BNBR.JK", "BNGA.JK", "BNII.JK", "BNLI.JK", "BOLT.JK", "BPFI.JK", "BPII.JK", "BRAM.JK", "BRMS.JK", "BRNA.JK", "BRPT.JK", "BSDE.JK", "BSIM.JK", "BSSR.JK", "BSWD.JK", "BTEK.JK", "BTEL.JK", "BTON.JK", "BTPN.JK", "BUDI.JK", "BUKK.JK", "BULL.JK", "BUMI.JK", "BUVA.JK", "BVIC.JK", "BWPT.JK", "BYAN.JK", "CANI.JK", "CASS.JK", "CEKA.JK", "CENT.JK", "CFIN.JK", "CINT.JK", "CITA.JK", "CLPI.JK", "CMNP.JK", "CMPP.JK", "CNKO.JK", "CNTX.JK", "COWL.JK", "CPIN.JK", "CPRO.JK", "CSAP.JK", "CTBN.JK", "CTRA.JK", "CTTH.JK", "DART.JK", "DEFI.JK", "DEWA.JK", "DGIK.JK", "DILD.JK", "DKFT.JK", "DLTA.JK", "DMAS.JK", "DNAR.JK", "DNET.JK", "DOID.JK", "DPNS.JK", "DSFI.JK", "DSNG.JK", "DSSA.JK", "DUTI.JK", "DVLA.JK", "DYAN.JK", "ECII.JK", "EKAD.JK", "ELSA.JK", "ELTY.JK", "EMDE.JK", "EMTK.JK", "ENRG.JK", "EPMT.JK", "ERAA.JK", "ERTX.JK", "ESSA.JK", "ESTI.JK", "ETWA.JK", "EXCL.JK", "FAST.JK", "FASW.JK", "FISH.JK", "FMII.JK", "FORU.JK", "FPNI.JK", "FREN.JK", "GAMA.JK", "GDST.JK", "GDYR.JK", "GEMA.JK", "GEMS.JK", "GGRM.JK", "GIAA.JK", "GJTL.JK", "GLOB.JK", "GMTD.JK", "GOLD.JK", "GOLL.JK", "GPRA.JK", "GSMF.JK", "GTBO.JK", "GWSA.JK", "GZCO.JK", "HADE.JK", "HDFA.JK", "HDTX.JK", "HERO.JK", "HEXA.JK", "HITS.JK", "HMSP.JK", "HOME.JK", "HOTL.JK", "HRUM.JK", "IATA.JK", "IBFN.JK", "IBST.JK", "ICBP.JK", "ICON.JK", "IGAR.JK", "IIKP.JK", "IKAI.JK", "IKBI.JK", "IMAS.JK", "IMJS.JK", "IMPC.JK", "INAF.JK", "INAI.JK", "INCI.JK", "INCO.JK", "INDF.JK", "INDR.JK", "INDS.JK", "INDX.JK", "INDY.JK", "INKP.JK", "INPC.JK", "INPP.JK", "INRU.JK", "INTA.JK", "INTD.JK", "INTP.JK", "JIHD.JK", "JKON.JK", "JKSW.JK", "JPFA.JK", "JRPT.JK", "JSMR.JK", "JSPT.JK", "JTPE.JK", "KAEF.JK", "KARW.JK", "KBLI.JK", "KBLM.JK", "KBLV.JK", "KBRI.JK", "KDSI.JK", "KIAS.JK", "KICI.JK", "KIJA.JK", "KKGI.JK", "KLBF.JK", "KOBX.JK", "KOIN.JK", "KONI.JK", "KOPI.JK", "KPIG.JK", "KRAH.JK", "KRAS.JK", "KREN.JK", "LAPD.JK", "LCGP.JK", "LEAD.JK", "LINK.JK", "LION.JK", "LMAS.JK", "LMPI.JK", "LMSH.JK", "LPCK.JK", "LPGI.JK", "LPIN.JK", "LPKR.JK", "LPLI.JK", "LPPF.JK", "LPPS.JK", "LRNA.JK", "LSIP.JK", "LTLS.JK", "MAGP.JK", "MAIN.JK", "MAMI.JK", "MAPI.JK", "MASA.JK", "MAYA.JK", "MBAP.JK", "MBSS.JK", "MBTO.JK", "MCOR.JK", "MDIA.JK", "MDKA.JK", "MDLN.JK", "MDRN.JK", "MEDC.JK", "MEGA.JK", "MERK.JK", "META.JK", "MFIN.JK", "MFMI.JK", "MGNA.JK", "MICE.JK", "MIDI.JK", "MIKA.JK", "MIRA.JK", "MITI.JK", "MKPI.JK", "MLBI.JK", "MLIA.JK", "MLPL.JK", "MLPT.JK", "MMLP.JK", "MNCN.JK", "MPMX.JK", "MPPA.JK", "MRAT.JK", "MREI.JK", "MSKY.JK", "MTDL.JK", "MTFN.JK", "MTLA.JK", "MTSM.JK", "MYOH.JK", "MYOR.JK", "MYRX.JK", "MYTX.JK", "NELY.JK", "NIKL.JK", "NIPS.JK", "NIRO.JK", "NISP.JK", "NOBU.JK", "NRCA.JK", "OCAP.JK", "OKAS.JK", "OMRE.JK", "PADI.JK", "PALM.JK", "PANR.JK", "PANS.JK", "PBRX.JK", "PDES.JK", "PEGE.JK", "PGAS.JK", "PGLI.JK", "PICO.JK", "PJAA.JK", "PKPK.JK", "PLAS.JK", "PLIN.JK", "PNBN.JK", "PNBS.JK", "PNIN.JK", "PNLF.JK", "PNSE.JK", "POLY.JK", "POOL.JK", "PPRO.JK", "PRAS.JK", "PSAB.JK", "PSDN.JK", "PSKT.JK", "PTBA.JK", "PTIS.JK", "PTPP.JK", "PTRO.JK", "PTSN.JK", "PTSP.JK", "PUDP.JK", "PWON.JK", "PYFA.JK", "RAJA.JK", "RALS.JK", "RANC.JK", "RBMS.JK", "RDTX.JK", "RELI.JK", "RICY.JK", "RIGS.JK", "RIMO.JK", "RODA.JK", "ROTI.JK", "RUIS.JK", "SAFE.JK", "SAME.JK", "SCCO.JK", "SCMA.JK", "SCPI.JK", "SDMU.JK", "SDPC.JK", "SDRA.JK", "SGRO.JK", "SHID.JK", "SIDO.JK", "SILO.JK", "SIMA.JK", "SIMP.JK", "SIPD.JK", "SKBM.JK", "SKLT.JK", "SKYB.JK", "SMAR.JK", "SMBR.JK", "SMCB.JK", "SMDM.JK", "SMDR.JK", "SMGR.JK", "SMMA.JK", "SMMT.JK", "SMRA.JK", "SMRU.JK", "SMSM.JK", "SOCI.JK", "SONA.JK", "SPMA.JK", "SQMI.JK", "SRAJ.JK", "SRIL.JK", "SRSN.JK", "SRTG.JK", "SSIA.JK", "SSMS.JK", "SSTM.JK", "STAR.JK", "STTP.JK", "SUGI.JK", "SULI.JK", "SUPR.JK", "TALF.JK", "TARA.JK", "TAXI.JK", "TBIG.JK", "TBLA.JK", "TBMS.JK", "TCID.JK", "TELE.JK", "TFCO.JK", "TGKA.JK", "TIFA.JK", "TINS.JK", "TIRA.JK", "TIRT.JK", "TKIM.JK", "TLKM.JK", "TMAS.JK", "TMPO.JK", "TOBA.JK", "TOTL.JK", "TOTO.JK", "TOWR.JK", "TPIA.JK", "TPMA.JK", "TRAM.JK", "TRIL.JK", "TRIM.JK", "TRIO.JK", "TRIS.JK", "TRST.JK", "TRUS.JK", "TSPC.JK", "ULTJ.JK", "UNIC.JK", "UNIT.JK", "UNSP.JK", "UNTR.JK", "UNVR.JK", "VICO.JK", "VINS.JK", "VIVA.JK", "VOKS.JK", "VRNA.JK", "WAPO.JK", "WEHA.JK", "WICO.JK", "WIIM.JK", "WIKA.JK", "WINS.JK", "WOMF.JK", "WSKT.JK", "WTON.JK", "YPAS.JK", "YULE.JK", "ZBRA.JK", "SHIP.JK", "CASA.JK", "DAYA.JK", "DPUM.JK", "IDPR.JK", "JGLE.JK", "KINO.JK", "MARI.JK", "MKNT.JK", "MTRA.JK", "PRDA.JK", "BOGA.JK", "BRIS.JK", "PORT.JK", "CARS.JK", "MINA.JK", "FORZ.JK", "CLEO.JK", "TAMU.JK", "CSIS.JK", "TGRA.JK", "FIRE.JK", "TOPS.JK", "KMTR.JK", "ARMY.JK", "MAPB.JK", "WOOD.JK", "HRTA.JK", "MABA.JK", "HOKI.JK", "MPOW.JK", "MARK.JK", "NASA.JK", "MDKI.JK", "BELL.JK", "KIOS.JK", "GMFI.JK", "MTWI.JK", "ZINC.JK", "MCAS.JK", "PPRE.JK", "WEGE.JK", "PSSI.JK", "MORA.JK", "DWGL.JK", "PBID.JK", "JMAS.JK", "CAMP.JK", "IPCM.JK", "PCAR.JK", "LCKM.JK", "BOSS.JK", "HELI.JK", "JSKY.JK", "INPS.JK", "GHON.JK", "TDPM.JK", "DFAM.JK", "NICK.JK", "BTPS.JK", "SPTO.JK", "PRIM.JK", "HEAL.JK", "TRUK.JK", "PZZA.JK", "TUGU.JK", "MSIN.JK", "SWAT.JK", "KPAL.JK", "TNCA.JK", "MAPA.JK", "TCPI.JK", "IPCC.JK", "RISE.JK", "BPTR.JK", "POLL.JK", "NFCX.JK", "MGRO.JK", "NUSA.JK", "FILM.JK", "ANDI.JK", "LAND.JK", "MOLI.JK", "PANI.JK", "DIGI.JK", "CITY.JK", "SAPX.JK", "KPAS.JK", "SURE.JK", "HKMU.JK", "MPRO.JK", "DUCK.JK", "GOOD.JK", "SKRN.JK", "YELO.JK", "CAKK.JK", "SATU.JK", "SOSS.JK", "DEAL.JK", "POLA.JK", "DIVA.JK", "LUCK.JK", "URBN.JK", "SOTS.JK", "ZONE.JK", "PEHA.JK", "FOOD.JK", "BEEF.JK", "POLI.JK", "CLAY.JK", "NATO.JK", "JAYA.JK", "COCO.JK", "MTPS.JK", "CPRI.JK", "HRME.JK", "POSA.JK", "JAST.JK", "FITT.JK", "BOLA.JK", "CCSI.JK", "SFAN.JK", "POLU.JK", "KJEN.JK", "KAYU.JK", "ITIC.JK", "PAMG.JK", "IPTV.JK", "BLUE.JK", "ENVY.JK", "EAST.JK", "LIFE.JK", "FUJI.JK", "KOTA.JK", "INOV.JK", "ARKA.JK", "SMKL.JK", "HDIT.JK", "KEEN.JK", "BAPI.JK", "TFAS.JK", "GGRP.JK", "OPMS.JK", "NZIA.JK", "SLIS.JK", "PURE.JK", "IRRA.JK", "DMMX.JK", "SINI.JK", "WOWS.JK", "ESIP.JK", "TEBE.JK", "KEJU.JK", "PSGO.JK", "AGAR.JK", "IFSH.JK", "REAL.JK", "IFII.JK", "PMJS.JK", "UCID.JK", "GLVA.JK", "PGJO.JK", "AMAR.JK", "CSRA.JK", "INDO.JK", "AMOR.JK", "TRIN.JK", "DMND.JK", "PURA.JK", "PTPW.JK", "TAMA.JK", "IKAN.JK", "AYLS.JK", "DADA.JK", "ASPI.JK", "ESTA.JK", "BESS.JK", "AMAN.JK", "CARE.JK", "SAMF.JK", "SBAT.JK", "KBAG.JK", "CBMF.JK", "RONY.JK", "CSMI.JK", "BBSS.JK", "BHAT.JK", "CASH.JK", "TECH.JK", "EPAC.JK", "UANG.JK", "PGUN.JK", "SOFA.JK", "PPGL.JK", "TOYS.JK", "SGER.JK", "TRJA.JK", "PNGO.JK", "SCNP.JK", "BBSI.JK", "KMDS.JK", "PURI.JK", "SOHO.JK", "HOMI.JK", "ROCK.JK", "ENZO.JK", "PLAN.JK", "PTDU.JK", "ATAP.JK", "VICI.JK", "PMMP.JK", "WIFI.JK", "FAPA.JK", "DCII.JK", "KETR.JK", "DGNS.JK", "UFOE.JK", "BANK.JK", "WMUU.JK", "EDGE.JK", "UNIQ.JK", "BEBS.JK", "SNLK.JK", "ZYRX.JK", "LFLO.JK", "FIMP.JK", "TAPG.JK", "NPGF.JK", "LUCY.JK", "ADCP.JK", "HOPE.JK", "MGLV.JK", "TRUE.JK", "LABA.JK", "ARCI.JK", "IPAC.JK", "MASB.JK", "BMHS.JK", "FLMC.JK", "NICL.JK", "UVCR.JK", "BUKA.JK", "HAIS.JK", "OILS.JK", "GPSO.JK", "MCOL.JK", "RSGK.JK", "RUNS.JK", "SBMA.JK", "CMNT.JK", "GTSI.JK", "IDEA.JK", "KUAS.JK", "BOBA.JK", "MTEL.JK", "DEPO.JK", "BINO.JK", "CMRY.JK", "WGSH.JK", "TAYS.JK", "WMPP.JK", "RMKE.JK", "OBMD.JK", "AVIA.JK", "IPPE.JK", "NASI.JK", "BSML.JK", "DRMA.JK", "ADMR.JK", "SEMA.JK", "ASLC.JK", "NETV.JK", "BAUT.JK", "ENAK.JK", "NTBK.JK", "SMKM.JK", "STAA.JK", "NANO.JK", "BIKE.JK", "WIRG.JK", "SICO.JK", "GOTO.JK", "TLDN.JK", "MTMH.JK", "WINR.JK", "IBOS.JK", "OLIV.JK", "ASHA.JK", "SWID.JK", "TRGU.JK", "ARKO.JK", "CHEM.JK", "DEWI.JK", "AXIO.JK", "KRYA.JK", "HATM.JK", "RCCC.JK", "GULA.JK", "JARR.JK", "AMMS.JK", "RAFI.JK", "KKES.JK", "ELPI.JK", "EURO.JK", "KLIN.JK", "TOOL.JK", "BUAH.JK", "CRAB.JK", "MEDS.JK", "COAL.JK", "PRAY.JK", "CBUT.JK", "BELI.JK", "MKTR.JK", "OMED.JK", "BSBK.JK", "PDPP.JK", "KDTN.JK", "ZATA.JK", "NINE.JK", "MMIX.JK", "PADA.JK", "ISAP.JK", "VTNY.JK", "SOUL.JK", "ELIT.JK", "BEER.JK", "CBPE.JK", "SUNI.JK", "CBRE.JK", "WINE.JK", "BMBL.JK", "PEVE.JK", "LAJU.JK", "FWCT.JK", "NAYZ.JK", "IRSX.JK", "PACK.JK", "VAST.JK", "CHIP.JK", "HALO.JK", "KING.JK", "PGEO.JK", "FUTR.JK", "HILL.JK", "BDKR.JK", "PTMP.JK", "SAGE.JK", "TRON.JK", "CUAN.JK", "NSSS.JK", "GTRA.JK", "HAJJ.JK", "PIPA.JK", "NCKL.JK", "MENN.JK", "AWAN.JK", "MBMA.JK", "RAAM.JK", "DOOH.JK", "JATI.JK", "TYRE.JK", "MPXL.JK", "SMIL.JK", "KLAS.JK", "MAXI.JK", "VKTR.JK", "RELF.JK", "AMMN.JK", "CRSN.JK", "GRPM.JK", "WIDI.JK", "TGUK.JK", "INET.JK", "MAHA.JK", "RMKO.JK", "CNMA.JK", "FOLK.JK", "HBAT.JK", "GRIA.JK", "PPRI.JK", "ERAL.JK", "CYBR.JK", "MUTU.JK", "LMAX.JK", "HUMI.JK", "MSIE.JK", "RSCH.JK", "BABY.JK", "AEGS.JK", "IOTF.JK", "KOCI.JK", "PTPS.JK", "BREN.JK", "STRK.JK", "KOKA.JK", "LOPI.JK", "UDNG.JK", "RGAS.JK", "MSTI.JK", "IKPM.JK", "AYAM.JK", "SURI.JK", "ASLI.JK", "CGAS.JK", "NICE.JK", "MSJA.JK", "SMLE.JK", "ACRO.JK", "MANG.JK", "GRPH.JK", "SMGA.JK", "UNTD.JK", "TOSK.JK", "MPIX.JK", "ALII.JK", "MKAP.JK", "MEJA.JK", "LIVE.JK", "HYGN.JK", "BAIK.JK", "VISI.JK", "AREA.JK", "MHKI.JK", "ATLA.JK", "DATA.JK", "SOLA.JK", "BATR.JK", "SPRE.JK", "PART.JK", "GOLF.JK", "ISEA.JK", "BLES.JK", "GUNA.JK", "LABS.JK", "DOSS.JK", "NEST.JK", "PTMR.JK", "VERN.JK", "DAAZ.JK", "BOAT.JK", "OASA.JK", "POWR.JK", "INCF.JK", "WSBP.JK", "PBSA.JK", "IPOL.JK", "ISAT.JK", "ISSP.JK", "ITMA.JK", "ITMG.JK", "JAWA.JK", "JECC.JK", "NAIK.JK"
]

# Remove duplicates
tickers = list(set(tickers))

# Tick rules
def calculate_tick(price):
    if price < 200:
        return 1
    elif 200 <= price < 500:
        return 2
    elif 500 <= price < 2000:
        return 5
    elif 2000 <= price < 5000:
        return 10
    else:
        return 25

# Fetch data with delay between requests
def fetch_data():
    spread_data = []
    batch_size = 100  # Set the batch size to process tickers in smaller chunks
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        for ticker in batch:
            stock = yf.Ticker(ticker)
            try:
                data = stock.info
                bid, ask = data.get("bid"), data.get("ask")
                
                if bid and ask:
                    spread = ask - bid
                    tick = calculate_tick(bid)
                    real_spread = spread - (tick * 2)
                    spread_percent = (real_spread / bid) * 100 if bid > 0 else 0
                    gain_trade = (real_spread / bid) * 100 if bid > 0 else 0
                    
                    spread_data.append({
                        "Ticker": ticker, 
                        "Bid": bid, 
                        "Ask": ask, 
                        "Spread": spread, 
                        "Real Spread": real_spread, 
                        "Spread (%)": spread_percent,
                        "Gain/Trade (%)": gain_trade
                    })
                
                # Sleep for 1 second between requests to avoid rate limiting
                time.sleep(1)  # Adjust the delay time based on your needs

            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
                # You can also add a longer sleep time if you get rate limit errors
                time.sleep(5)  # Increased sleep on error to be more cautious
        
        # Sleep for 5 seconds after each batch to avoid being rate-limited
        time.sleep(5)
    
    return pd.DataFrame(spread_data)

# Fetch data initially
df = fetch_data()

# Display data
st.write("### Spread Data with Gain/Trade (%)")
st.dataframe(df)

# Top 3 by Gain/Trade (%)
st.write("### Top 3 Stocks by Gain/Trade (%)")
st.table(df.nlargest(5, "Gain/Trade (%)"))

# Visualization
if not df.empty:
    st.write("### Gain/Trade (%) Visualization")
    fig, ax = plt.subplots()
    df.dropna().plot.bar(x="Ticker", y="Gain/Trade (%)", ax=ax, color="blue", legend=False)
    plt.title("Gain/Trade (%) per Ticker")
    plt.xlabel("Ticker")
    plt.ylabel("Gain/Trade (%)")
    st.pyplot(fig)

# Refresh button
if st.button("Refresh Data"):
    df = fetch_data()
    st.dataframe(df)
