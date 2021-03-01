a4_q2_kb.txt contains some of the common diseases and their most common symptoms.

User can enter all the symptoms they are experiencing and the program will tell what disease they may have.

For Eg.

kb>load a4_q2_kb.txt
Rule 1 : anaemia <-- fatigue & shortness_of_breath & dizziness & headache & chest_pain

Rule 2 : malaria <-- fever & chills & headache & vomiting & fatigue

Rule 3 : covid_19 <-- fever & cough & fatigue

Rule 4 : flu <-- fever & cough & sore_throat & runny_nose & headache

Rule 5 : dengue <-- headache & muscle_pain & vomiting & rashes

Rule 6 : common_cold <-- runny_nose & sore_throat & sneezing & fever

Rule 7 : anxiety <-- restlessness & irritability & difficulty_contentrating & fast_heartbeat

Rule 8 : asthma <-- wheezing & shortness_of_breath & tight_chest & cough

Rule 9 : bladder_cancer <-- blood_in_urine & frequent_urination & burning_sensation_when_urinate

Rule 10 : breast_cancer <-- lump_in_breast & change_in_shape_of_breast & dimpling_breast_skin & rash_on_or_around_nipples

Rule 11 : bronchitis <-- sore_throat & headache & runny_nose & fatigue

Rule 12 : chest_infection <-- cough & Phlegm & shortness_of_breath & fever & chest_pain 

Rule 13 : chickenpox <-- red_rash_covering_all_body

Rule 14 : cervical_cancer <-- unusual_vaginal_bleeding

Rule 15 : chronic_kidney_disease <-- weight_loss & swollen_ankles & shortness_of_breath & vomiting & Muscle_cramps & insomnia

Rule 16 : cold_sore <-- swollen_gums & sore_throat & fever & vomiting & headache

Rule 17 : constipation <-- stomach_ache & feeling_bloated & feeling_sick & loss_of_appetite

Rule 18 : dehydration <-- dizziness & headache & fatigue & dry_mouth

Rule 19 : diabetes <-- feeling_very_thirsty & frequent_urination & fatigue & weight_loss & blurred_vision

Rule 20 : depression <-- feeling_hopeless & feeling_sad & lack_of_interest_in_anything

Rule 21 : diarrhoea <-- stomach_cramps & vomiting & headache & loss_of_appetite

Rule 22 : ebola_virus <-- fever & headache & muscle_pain & sore_throat & muscle_weakness

Rule 23 : eye_cancer <-- blurred_vision & buldging_eye & lump_on_eyelid & eye_pain

Rule 24 : gallstones <-- severe_abdominal_pain

Rule 25 : gum_disease <-- swollen_gums & gums_bleeding_after_brushing

Rule 26 : heart_failure <-- shortness_of_breath & fatigue & leg_swelling & loss_of_appetite

Rule 27 : hiv <-- fever & sore_throat & body_rash

Rule 28 : indigestion <-- feeling_uncomfortable & bloating & vomiting

Rule 29 : insomnia <-- trouble_sleeping

Rule 30 : kidney_stones <-- lower_back_ache & severe_abdominal_pain & vomiting

Rule 31 : kidney_infection <-- lower_back_ache & fever & loss_of_appetite & Diarrhoea & fatigue

Rule 32 : lung_cancer <-- cough & coughing_blood & shortness_of_breath & fatigue & chest_pain

Rule 33 : malnutrition <-- fatigue & frequently_getting_sick & Depression & difficulty_contentrating

Rule 34 : stomach_cancer <-- indigestion & heartburn & bloating & stomach_ache & difficulty_swallowing & vomiting

Rule 35 : thyroid_cancer <-- sore_throat & hoarseness & neck_fain

Rule 36 : tuberculosis <-- night_sweats & fever & loss_of_appetite & fatigue & coughing_blood & chest_pain

36 rules added

kb>tell fever cough fatigue sore_throat runny_nose headache
" fever " added to kb

" cough " added to kb

" fatigue " added to kb

" sore_throat " added to kb

" runny_nose " added to kb

" headache " added to kb

kb>infer_all
Newly inferred items : ['covid_19', 'flu', 'bronchitis'] 

Already known truth : ['fever', 'cough', 'fatigue', 'sore_throat', 'runny_nose', 'headache'] 

In this example user entered ['fever', 'cough', 'fatigue', 'sore_throat', 'runny_nose', 'headache'] these
as symptoms and the program told them that they might have ['covid_19', 'flu', 'bronchitis'] any of these according to the symptoms told.