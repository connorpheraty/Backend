from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from flask_cors import CORS
import json

application = app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)



@app.route('/')
def root():
    """
    Testing
    """
    return "Test Successful"

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
  # Get Json request
  # Tokenize request
  # Match tokens with keywords in dataframe
  # Isolate relevant results
  # Return relevant information pertaining to isolated results

  #data = request.get_json(force=True)

  #query = data['query']
  #print(query)
  #Unpacking string query
  brief_title= {"4":"Widespread vs. Selective Screening for Hepatitis B Infection Prior to Chemotherapy",
                "12":"Sjogren-Larsson Syndrome: Natural History, Clinical Variation and Evaluation of Biochemical Markers",
                "13":"Functional MR-guided Stereotactic Body Radiation Therapy of Prostate Cancer",
                "15":"Narcotic vs. Non-narcotic Pain Study Protocol",
                "32":"In Situ Vaccine for Low-Grade Lymphoma: Combination of Intratumoral Flt3L and Poly-ICLC With Low-Dose Radiotherapy",
                "34":"HIV-related Accelerated Aging of the Airway Epithelium",
                "45":"Predictive Clinical and Biological Parameters in Gynecological Cancer - GC-BIO-IPC 2013-010",
                "70":"Assessment of Early Treatment Response by Diffusion and Perfusion MRI in Patients With Brain Metastasis",
                "80":"Cancer and Anesthesia: Survival After Radical Surgery - a Comparison Between Propofol or Sevoflurane Anesthesia",
                "85":"Phase 1b Study of PD-0332991 in Combination With T-DM1(Trastuzumab-DM1)"}

  brief_summary = {"4":"\n\n      The goal of this clinical research study is to learn about testing patients for viral\n      infections before chemotherapy. Researchers want to learn which patients are at higher risk\n      for these infections so that, in the future, patients might be able to be tested more\n      effectively.\n    \n",
                  "12":"\n\n      Sjogren-Larsson syndrome (SLS) is a rare genetic disease in which patients typically exhibit\n      ichthyosis (dry, scaly skin), intellectual disability, spasticity, seizures and a distinctive\n      maculopathy. The purpose of this study is to define the clinical spectrum and natural history\n      of Sjogren-Larsson syndrome, and identify biomarkers that correlate with disease phenotype\n      while establishing a registry for future investigations of biochemical pathogenesis and\n      therapy.\n    \n",
                  "13":"\n\n      To improve radiation therapy of prostate cancer, the investigators must be able to accurately\n      identify the tumour. By using advanced functional imaging techniques available on\n      state-of-the-art MRI scanners to clearly show the specific location of the tumour inside the\n      prostate, the investigators can use advanced radiation therapy techniques to specifically\n      target the tumor and control it with as few radiotherapy clinic visits as possible. This is\n      different than current techniques which treat the whole prostate gland to the same dose,\n      delivered over 7-8 weeks of daily radiotherapy visits. By increasing the radiation dose to\n      the active tumor while still maintaining adequate radiation dose to the rest of the prostate,\n      the investigators hope to better control prostate cancer and reduce complications to nearby\n      normal tissues.\n    \n",
                  "15":"\n\n      The purposes of this noninferiority randomized clinical trial are to:\n\n        1. determine whether the most commonly used commonly used non-narcotic analgesic (ibuprofen\n           600 mg + acetaminophen 325 mg) provides pain relief that is not unacceptably worse than\n           the most commonly prescribed narcotic containing analgesic (hydrocodone 5 mg. +\n           acetaminophen 325 mg, equivalent to Norco 5\/325) in patients undergoing carpal tunnel\n           release.\n\n        2. Determine whether the following covariates affect pain level following surgery or\n           medication usage: gender, country (US\/Canada), pre-operative CTS symptoms, site, workers\n           compensation status and employment status (employed\/self-employed\/unemployed-able to\n           work\/unemployed-unable to work)\n    \n",
                  "32":"\n\n      Our recent trials combining local radiotherapy with intratumoral administration of TLR\n      agonists - referred to as 'in situ vaccination' - for patients with low-grade lymphoma\n      demonstrated safety, induction of anti-tumor CD8 T cell responses and partial and complete\n      remissions of patients' non-irradiated sites of disease with complete remissions lasting from\n      months to more than three years.\n\n      This iteration of the in situ vaccine approach builds on our prior work in ways that should\n      improve its efficacy, by adding Flt3L and changing the toll-like receptors (TLR) agonist to\n      poly-ICLC -an optimal TLR agonist for the type of dendritic cells (DC) recruited by Flt3L.\n      The vaccine is thus in 3 phases:\n\n        1. intratumoral Flt3L administration recruits DC to the tumor\n\n        2. low-dose radiotherapy to release tumor antigens\n\n        3. intratumoral poly-ICLC administration activates tumor-antigen loaded DC\n    \n",
                  "34":"\n\n      In cigarette smokers that are HIV+, one of the most common HIV-associated non-AIDS conditions\n      is the accelerated development of chronic obstructive pulmonary disease (COPD), a disorder\n      associated with significant morbidity and mortality. Based on the knowledge that COPD in\n      smokers starts in the small airway epithelium, this study is focused on examining the\n      hypothesis that the accelerated development of COPD associated with HIV infection results, in\n      part, from an interaction of HIV directly on the small airway epithelium or through infection\n      of cellular components of the immune system, with mediators released by these immune cells\n      evoking premature biologic aging of the small airway epithelium. By identifying the early\n      events in the pathogenesis of the HIV-associated accelerated COPD in smokers, we aim to\n      identify biologic targets to which pharmacologic therapies could be addressed.\n    \n",
                  "45":"\n\n      Research of predictive clinical and biological factors in breast cancer : genomic, proteomic,\n      mutation\n    \n",
                  "70":"\n\n      Magnetic resonance imaging (MRI) is a diagnostic study that makes pictures of organs of the\n      body using magnetic field and radio frequency pulses that can not be felt. The purpose of\n      this study is to determine if new imaging methods can help tumor evaluation in the brain. The\n      extra images will be obtained using diffusion and perfusion MRI techniques to assess early\n      treatment response in patients with brain metastasis, and will be compared to methods\n      currently being used.\n    \n",
                  "80":"\n\n      The purpose of this study is to determine whether anesthesia maintained with propofol results\n      in better one- and five-year-survival than anesthesia maintained with sevoflurane.\n    \n",
                  "85":"\n\n      Standard of care:\n\n      Treatment with Trastuzumab\n\n      Experimental:\n\n      21-Day Cycle of Combination therapy with T-DM1 intravenously on Day 1 and oral PD-0332991 on\n      Days 5-18\n\n      Study Design and Methodology:\n\n      This is a phase 1B inter-patient dose escalation study of PD-0332991 in combination with\n      T-DM1 in patients with recurrent or metastatic HER2-positive breast cancer after prior\n      trastuzumab or other HER2-directed therapies.\n\n      The subjects will be administered T-DM1 by intravenous infusion at 3.6 mg\/kg for 90 minutes\n      on day 1 of each 21 day cycle. Infusion timing may vary from 30-90 minutes depending on how\n      well the subject tolerates the treatment.\n\n      A standard 3+3 trial design will be used for PD-0332991 dose escalation cohorts.The dosing of\n      PD-0332991 will be divided into 3 cohorts, the subjects will receive PD-0332991 on days 5-18\n      of each 21 day cycle.\n\n      Cohort 1 : PD-0332991 - 100 mg daily (oral) Cohort 2 : PD-0332991 - 150 mg daily (oral)\n      Cohort 3 : PD-0332991 - 200 mg daily (oral)\n\n      The 3+3 design entails that if one patient out of the first three patients has a DLT, up to\n      three additional patients will be entered at that dose level\n\n      Treatment cycles will continue until disease progression or withdrawal from study.\n    \n"}
  condition = {"4":"Cancer",
              "12":"Sjogren-Larsson Syndrome (SLS)",
              "13":"Prostatic Neoplasms",
              "15":"Carpal Tunnel",
              "32":"Low-Grade B-cell Lymphoma",
              "34":"HIV",
              "45":"Ovarian Cancer",
              "70":"Brain Cancer",
              "80":"Breast Neoplasms",
              "85":"Advanced Breast Cancer"}
              
  intervention_name={"4":"HBV screening tests",
                      "12":"null",
                      "13":"Stereotactic body RT with MR-guided boost",
                      "15":"Narcotic",
                      "32":"rhuFlt3L\/CDX-301",
                      "34":"null",
                      "45":"gynecological cancer",
                      "70":"MRI",
                      "80":"Propofol",
                      "85":"PD-0332991 and T-DM1"}
  phase={"4":"null",
          "12":"null",
          "13":"null",
          "15":"Phase 4",
          "32":"Phase 1\/Phase 2",
          "34":"null",
          "45":"null",
          "70":"null",
          "80":"Phase 4",
          "85":"Phase 1"}

  city={"4":"Houston",
         "12":"Omaha",
         "13":"Winnipeg",
         "15":"Philadelphia",
         "32":"New York",
         "34":"New York",
         "45":"Marseille",
         "70":"New York",
         "80":"Beijing",
         "85":"Dallas"}

  state={"4":"Texas",
          "12":"Nebraska",
          "13":"Manitoba",
          "15":"Pennsylvania",
          "32":"New York",
          "34":"New York",
          "45":"null",
          "70":"New York",
          "80":"null",
          "85":"Texas"}

  country={"4":"United States",
            "12":"United States",
            "13":"Canada",
            "15":"United States",
            "32":"United States",
            "34":"United States",
            "45":"France",
            "70":"United States",
            "80":"China",
            "85":"United States"}
          

  return json_response(brief_title=brief_title, brief_summary=brief_summary, condition=condition,
                       intervention_name=intervention_name, phase=phase, city=city,
                       state=state, country=country)
  
if __name__ == '__main__':
        application.run()