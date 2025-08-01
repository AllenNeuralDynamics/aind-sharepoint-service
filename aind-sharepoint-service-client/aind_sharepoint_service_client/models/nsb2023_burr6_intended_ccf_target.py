# coding: utf-8

"""
    aind-sharepoint-service

     ## aind-sharepoint-service  Service to pull data from Sharepoint.  

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NSB2023Burr6IntendedCcfTarget(str, Enum):
    """
    Enum class for Burr 6 Intended CCF Target.
    """

    """
    allowed enum values
    """
    FRP__FRONTAL_POLE_CEREBRA = 'FRP - Frontal pole cerebral cortex'
    M_OP__PRIMARY_MOTOR_AREA = 'MOp - Primary motor area'
    M_OS__SECONDARY_MOTOR_ARE = 'MOs - Secondary motor area'
    S_SP_N__PRIMARY_SOMATOSEN = 'SSp-n - Primary somatosensory area nose'
    S_SP_BFD__PRIMARY_SOMATOS = 'SSp-bfd - Primary somatosensory area barrel field'
    S_SP_LL__PRIMARY_SOMATOSE = 'SSp-ll - Primary somatosensory area lower limb'
    S_SP_M__PRIMARY_SOMATOSEN = 'SSp-m - Primary somatosensory area mouth'
    S_SP_UL__PRIMARY_SOMATOSE = 'SSp-ul - Primary somatosensory area upper limb'
    S_SP_TR__PRIMARY_SOMATOSE = 'SSp-tr - Primary somatosensory area trunk'
    S_SP_UN__PRIMARY_SOMATOSE = 'SSp-un - Primary somatosensory area unassigned'
    S_SS__SUPPLEMENTAL_SOMATO = 'SSs - Supplemental somatosensory area'
    GU__GUSTATORY_AREAS = 'GU - Gustatory areas'
    VISC__VISCERAL_AREA = 'VISC - Visceral area'
    AU_DD__DORSAL_AUDITORY_AR = 'AUDd - Dorsal auditory area'
    AU_DP__PRIMARY_AUDITORY_A = 'AUDp - Primary auditory area'
    AU_DPO__POSTERIOR_AUDITOR = 'AUDpo - Posterior auditory area'
    AU_DV__VENTRAL_AUDITORY_A = 'AUDv - Ventral auditory area'
    VI_SAL__ANTEROLATERAL_VIS = 'VISal - Anterolateral visual area'
    VI_SAM__ANTEROMEDIAL_VISU = 'VISam - Anteromedial visual area'
    VI_SL__LATERAL_VISUAL_ARE = 'VISl - Lateral visual area'
    VI_SP__PRIMARY_VISUAL_ARE = 'VISp - Primary visual area'
    VI_SPL__POSTEROLATERAL_VI = 'VISpl - Posterolateral visual area'
    VI_SPM_POSTEROMEDIAL_VISU = 'VISpm - posteromedial visual area'
    VI_SLI__LATEROINTERMEDIAT = 'VISli - Laterointermediate area'
    VI_SPOR__POSTRHINAL_AREA = 'VISpor - Postrhinal area'
    AC_AD__ANTERIOR_CINGULATE = 'ACAd - Anterior cingulate area dorsal part'
    AC_AV__ANTERIOR_CINGULATE = 'ACAv - Anterior cingulate area ventral part'
    PL__PRELIMBIC_AREA = 'PL - Prelimbic area'
    ILA__INFRALIMBIC_AREA = 'ILA - Infralimbic area'
    OR_BL__ORBITAL_AREA_LATER = 'ORBl - Orbital area lateral part'
    OR_BM__ORBITAL_AREA_MEDIA = 'ORBm - Orbital area medial part'
    OR_BV__ORBITAL_AREA_VENTR = 'ORBv - Orbital area ventral part'
    OR_BVL__ORBITAL_AREA_VENT = 'ORBvl - Orbital area ventrolateral part'
    A_ID__AGRANULAR_INSULAR_A = 'AId - Agranular insular area dorsal part'
    A_IP__AGRANULAR_INSULAR_A = 'AIp - Agranular insular area posterior part'
    A_IV__AGRANULAR_INSULAR_A = 'AIv - Agranular insular area ventral part'
    RS_PAGL__RETROSPLENIAL_AR = 'RSPagl - Retrosplenial area lateral agranular part'
    RS_PD__RETROSPLENIAL_AREA = 'RSPd - Retrosplenial area dorsal part'
    RS_PV__RETROSPLENIAL_AREA = 'RSPv - Retrosplenial area ventral part'
    VI_SA__ANTERIOR_AREA = 'VISa - Anterior area'
    VI_SRL__ROSTROLATERAL_VIS = 'VISrl - Rostrolateral visual area'
    T_EA__TEMPORAL_ASSOCIATIO = 'TEa - Temporal association areas'
    PERI__PERIRHINAL_AREA = 'PERI - Perirhinal area'
    ECT__ECTORHINAL_AREA = 'ECT - Ectorhinal area'
    MOB__MAIN_OLFACTORY_BULB = 'MOB - Main olfactory bulb'
    AOB__ACCESSORY_OLFACTORY = 'AOB - Accessory olfactory bulb'
    AON__ANTERIOR_OLFACTORY_N = 'AON - Anterior olfactory nucleus'
    T_TD__TAENIA_TECTA_DORSAL = 'TTd - Taenia tecta dorsal part'
    T_TV__TAENIA_TECTA_VENTRA = 'TTv - Taenia tecta ventral part'
    DP__DORSAL_PEDUNCULAR_ARE = 'DP - Dorsal peduncular area'
    PIR__PIRIFORM_AREA = 'PIR - Piriform area'
    NLOT__NUCLEUS_OF_THE_LATE = 'NLOT - Nucleus of the lateral olfactory tract'
    CO_AA__CORTICAL_AMYGDALAR = 'COAa - Cortical amygdalar area anterior part'
    CO_AP__CORTICAL_AMYGDALAR = 'COAp - Cortical amygdalar area posterior part'
    PAA__PIRIFORM_AMYGDALAR_A = 'PAA - Piriform-amygdalar area'
    TR__POSTPIRIFORM_TRANSITI = 'TR - Postpiriform transition area'
    CA1__FIELD_CA1 = 'CA1 - Field CA1'
    CA2__FIELD_CA2 = 'CA2 - Field CA2'
    CA3__FIELD_CA3 = 'CA3 - Field CA3'
    DG__DENTATE_GYRUS = 'DG - Dentate gyrus'
    FC__FASCIOLA_CINEREA = 'FC - Fasciola cinerea'
    IG__INDUSEUM_GRISEUM = 'IG - Induseum griseum'
    EN_TL__ENTORHINAL_AREA_LA = 'ENTl - Entorhinal area lateral part'
    EN_TM__ENTORHINAL_AREA_ME = 'ENTm - Entorhinal area medial part dorsal zone'
    PAR__PARASUBICULUM = 'PAR - Parasubiculum'
    POST__POSTSUBICULUM = 'POST - Postsubiculum'
    PRE__PRESUBICULUM = 'PRE - Presubiculum'
    SUB__SUBICULUM = 'SUB - Subiculum'
    PRO_S__PROSUBICULUM = 'ProS - Prosubiculum'
    HATA__HIPPOCAMPO_AMYGDALA = 'HATA - Hippocampo-amygdalar transition area'
    A_PR__AREA_PROSTRIATA = 'APr - Area prostriata'
    CLA__CLAUSTRUM = 'CLA - Claustrum'
    E_PD__ENDOPIRIFORM_NUCLEU = 'EPd - Endopiriform nucleus dorsal part'
    E_PV__ENDOPIRIFORM_NUCLEU = 'EPv - Endopiriform nucleus ventral part'
    LA__LATERAL_AMYGDALAR_NUC = 'LA - Lateral amygdalar nucleus'
    BLA__BASOLATERAL_AMYGDALA = 'BLA - Basolateral amygdalar nucleus'
    BMA__BASOMEDIAL_AMYGDALAR = 'BMA - Basomedial amygdalar nucleus'
    PA__POSTERIOR_AMYGDALAR_N = 'PA - Posterior amygdalar nucleus'
    CP__CAUDOPUTAMEN = 'CP - Caudoputamen'
    ACB__NUCLEUS_ACCUMBENS = 'ACB - Nucleus accumbens'
    FS__FUNDUS_OF_STRIATUM = 'FS - Fundus of striatum'
    OT__OLFACTORY_TUBERCLE = 'OT - Olfactory tubercle'
    L_SC__LATERAL_SEPTAL_NUCL = 'LSc - Lateral septal nucleus caudal (caudodorsal) part'
    L_SR__LATERAL_SEPTAL_NUCL = 'LSr - Lateral septal nucleus rostral (rostroventral) part'
    L_SV__LATERAL_SEPTAL_NUCL = 'LSv - Lateral septal nucleus ventral part'
    SF__SEPTOFIMBRIAL_NUCLEUS = 'SF - Septofimbrial nucleus'
    SH__SEPTOHIPPOCAMPAL_NUCL = 'SH - Septohippocampal nucleus'
    AAA__ANTERIOR_AMYGDALAR_A = 'AAA - Anterior amygdalar area'
    BA__BED_NUCLEUS_OF_THE_AC = 'BA - Bed nucleus of the accessory olfactory tract'
    CEA__CENTRAL_AMYGDALAR_NU = 'CEA - Central amygdalar nucleus'
    IA__INTERCALATED_AMYGDALA = 'IA - Intercalated amygdalar nucleus'
    MEA__MEDIAL_AMYGDALAR_NUC = 'MEA - Medial amygdalar nucleus'
    G_PE__GLOBUS_PALLIDUS_EXT = 'GPe - Globus pallidus external segment'
    G_PI__GLOBUS_PALLIDUS_INT = 'GPi - Globus pallidus internal segment'
    SI__SUBSTANTIA_INNOMINATA = 'SI - Substantia innominata'
    MA__MAGNOCELLULAR_NUCLEUS = 'MA - Magnocellular nucleus'
    MS__MEDIAL_SEPTAL_NUCLEUS = 'MS - Medial septal nucleus'
    NDB__DIAGONAL_BAND_NUCLEU = 'NDB - Diagonal band nucleus'
    TRS__TRIANGULAR_NUCLEUS_O = 'TRS - Triangular nucleus of septum'
    BST__BED_NUCLEI_OF_THE_ST = 'BST - Bed nuclei of the stria terminalis'
    VAL__VENTRAL_ANTERIOR_LAT = 'VAL - Ventral anterior-lateral complex of the thalamus'
    VM__VENTRAL_MEDIAL_NUCLEU = 'VM - Ventral medial nucleus of the thalamus'
    VPL__VENTRAL_POSTEROLATER = 'VPL - Ventral posterolateral nucleus of the thalamus'
    VP_LPC__VENTRAL_POSTEROLA = 'VPLpc - Ventral posterolateral nucleus of the thalamus parvicellular part'
    VPM__VENTRAL_POSTEROMEDIA = 'VPM - Ventral posteromedial nucleus of the thalamus'
    VVP_MPC__VENTRAL_POSTEROME = 'VPMpc - Ventral posteromedial nucleus of the thalamus parvicellular part'
    PO_T__POSTERIOR_TRIANGULA = 'PoT - Posterior triangular thalamic nucleus'
    SPF__SUBPARAFASCICULAR_NU = 'SPF - Subparafascicular nucleus'
    SPA__SUBPARAFASCICULAR_AR = 'SPA - Subparafascicular area'
    PP__PERIPEDUNCULAR_NUCLEU = 'PP - Peripeduncular nucleus'
    MG__MEDIAL_GENICULATE_COM = 'MG - Medial geniculate complex'
    L_GD__DORSAL_PART_OF_THE = 'LGd - Dorsal part of the lateral geniculate complex'
    LP__LATERAL_POSTERIOR_NUC = 'LP - Lateral posterior nucleus of the thalamus'
    PO__POSTERIOR_COMPLEX_OF = 'PO - Posterior complex of the thalamus'
    POL__POSTERIOR_LIMITING_N = 'POL - Posterior limiting nucleus of the thalamus'
    SGN__SUPRAGENICULATE_NUCL = 'SGN - Suprageniculate nucleus'
    ETH__ETHMOID_NUCLEUS_OF_T = 'Eth - Ethmoid nucleus of the thalamus'
    AV__ANTEROVENTRAL_NUCLEUS = 'AV - Anteroventral nucleus of thalamus'
    AM__ANTEROMEDIAL_NUCLEUS = 'AM - Anteromedial nucleus'
    AD__ANTERODORSAL_NUCLEUS = 'AD - Anterodorsal nucleus'
    IAM__INTERANTEROMEDIAL_NU = 'IAM - Interanteromedial nucleus of the thalamus'
    IAD__INTERANTERODORSAL_NU = 'IAD - Interanterodorsal nucleus of the thalamus'
    LD__LATERAL_DORSAL_NUCLEU = 'LD - Lateral dorsal nucleus of thalamus'
    IMD__INTERMEDIODORSAL_NUC = 'IMD - Intermediodorsal nucleus of the thalamus'
    MD__MEDIODORSAL_NUCLEUS_O = 'MD - Mediodorsal nucleus of thalamus'
    SMT__SUBMEDIAL_NUCLEUS_OF = 'SMT - Submedial nucleus of the thalamus'
    PR__PERIREUNENSIS_NUCLEUS = 'PR - Perireunensis nucleus'
    PVT__PARAVENTRICULAR_NUCL = 'PVT - Paraventricular nucleus of the thalamus'
    PT__PARATAENIAL_NUCLEUS = 'PT - Parataenial nucleus'
    RE__NUCLEUS_OF_REUNIENS = 'RE - Nucleus of reuniens'
    XI__XIPHOID_THALAMIC_NUCL = 'Xi - Xiphoid thalamic nucleus'
    RH__RHOMBOID_NUCLEUS = 'RH - Rhomboid nucleus'
    CM__CENTRAL_MEDIAL_NUCLEU = 'CM - Central medial nucleus of the thalamus'
    PCN__PARACENTRAL_NUCLEUS = 'PCN - Paracentral nucleus'
    CL__CENTRAL_LATERAL_NUCLE = 'CL - Central lateral nucleus of the thalamus'
    PF__PARAFASCICULAR_NUCLEU = 'PF - Parafascicular nucleus'
    PIL__POSTERIOR_INTRALAMIN = 'PIL - Posterior intralaminar thalamic nucleus'
    RT__RETICULAR_NUCLEUS_OF = 'RT - Reticular nucleus of the thalamus'
    IGL__INTERGENICULATE_LEAF = 'IGL - Intergeniculate leaflet of the lateral geniculate complex'
    INT_G__INTERMEDIATE_GENIC = 'IntG - Intermediate geniculate nucleus'
    L_GV__VENTRAL_PART_OF_THE = 'LGv - Ventral part of the lateral geniculate complex'
    SUB_G__SUBGENICULATE_NUCL = 'SubG - Subgeniculate nucleus'
    MH__MEDIAL_HABENULA = 'MH - Medial habenula'
    LH__LATERAL_HABENULA = 'LH - Lateral habenula'
    SO__SUPRAOPTIC_NUCLEUS = 'SO - Supraoptic nucleus'
    PVH__PARAVENTRICULAR_HYPO = 'PVH - Paraventricular hypothalamic nucleus'
    P_VA__PERIVENTRICULAR_HYP = 'PVa - Periventricular hypothalamic nucleus anterior part'
    P_VI__PERIVENTRICULAR_HYP = 'PVi - Periventricular hypothalamic nucleus intermediate part'
    ARH__ARCUATE_HYPOTHALAMIC = 'ARH - Arcuate hypothalamic nucleus'
    ADP__ANTERODORSAL_PREOPTI = 'ADP - Anterodorsal preoptic nucleus'
    AVP__ANTEROVENTRAL_PREOPT = 'AVP - Anteroventral preoptic nucleus'
    AVPV__ANTEROVENTRAL_PERIV = 'AVPV - Anteroventral periventricular nucleus'
    DMH__DORSOMEDIAL_NUCLEUS = 'DMH - Dorsomedial nucleus of the hypothalamus'
    MEPO__MEDIAN_PREOPTIC_NUC = 'MEPO - Median preoptic nucleus'
    MPO__MEDIAL_PREOPTIC_AREA = 'MPO - Medial preoptic area'
    PS__PARASTRIAL_NUCLEUS = 'PS - Parastrial nucleus'
    P_VP__PERIVENTRICULAR_HYP = 'PVp - Periventricular hypothalamic nucleus posterior part'
    P_VPO__PERIVENTRICULAR_HY = 'PVpo - Periventricular hypothalamic nucleus preoptic part'
    SBPV__SUBPARAVENTRICULAR = 'SBPV - Subparaventricular zone'
    SCH__SUPRACHIASMATIC_NUCL = 'SCH - Suprachiasmatic nucleus'
    SFO__SUBFORNICAL_ORGAN = 'SFO - Subfornical organ'
    VMPO__VENTROMEDIAL_PREOPT = 'VMPO - Ventromedial preoptic nucleus'
    VLPO__VENTROLATERAL_PREOP = 'VLPO - Ventrolateral preoptic nucleus'
    AHN__ANTERIOR_HYPOTHALAMI = 'AHN - Anterior hypothalamic nucleus'
    LM__LATERAL_MAMMILLARY_NU = 'LM - Lateral mammillary nucleus'
    MM__MEDIAL_MAMMILLARY_NUC = 'MM - Medial mammillary nucleus'
    SUM__SUPRAMAMMILLARY_NUCL = 'SUM - Supramammillary nucleus'
    TM__TUBEROMAMMILLARY_NUCL = 'TM - Tuberomammillary nucleus'
    MPN__MEDIAL_PREOPTIC_NUCL = 'MPN - Medial preoptic nucleus'
    P_MD__DORSAL_PREMAMMILLAR = 'PMd - Dorsal premammillary nucleus'
    P_MV__VENTRAL_PREMAMMILLA = 'PMv - Ventral premammillary nucleus'
    PV_HD__PARAVENTRICULAR_HY = 'PVHd - Paraventricular hypothalamic nucleus descending division'
    VMH__VENTROMEDIAL_HYPOTHA = 'VMH - Ventromedial hypothalamic nucleus'
    PH__POSTERIOR_HYPOTHALAMI = 'PH - Posterior hypothalamic nucleus'
    LHA__LATERAL_HYPOTHALAMIC = 'LHA - Lateral hypothalamic area'
    LPO__LATERAL_PREOPTIC_ARE = 'LPO - Lateral preoptic area'
    PSTN__PARASUBTHALAMIC_NUC = 'PSTN - Parasubthalamic nucleus'
    PE_F__PERIFORNICAL_NUCLEU = 'PeF - Perifornical nucleus'
    RCH__RETROCHIASMATIC_AREA = 'RCH - Retrochiasmatic area'
    STN__SUBTHALAMIC_NUCLEUS = 'STN - Subthalamic nucleus'
    TU__TUBERAL_NUCLEUS = 'TU - Tuberal nucleus'
    ZI__ZONA_INCERTA = 'ZI - Zona incerta'
    S_CS__SUPERIOR_COLLICULUS = 'SCs - Superior colliculus sensory related'
    IC__INFERIOR_COLLICULUS = 'IC - Inferior colliculus'
    NB__NUCLEUS_OF_THE_BRACHI = 'NB - Nucleus of the brachium of the inferior colliculus'
    SAG__NUCLEUS_SAGULUM = 'SAG - Nucleus sagulum'
    PBG__PARABIGEMINAL_NUCLEU = 'PBG - Parabigeminal nucleus'
    S_NR__SUBSTANTIA_NIGRA_RE = 'SNr - Substantia nigra reticular part'
    VTA__VENTRAL_TEGMENTAL_AR = 'VTA - Ventral tegmental area'
    PN__PARANIGRAL_NUCLEUS = 'PN - Paranigral nucleus'
    RR__MIDBRAIN_RETICULAR_NU = 'RR - Midbrain reticular nucleus retrorubral area'
    MRN__MIDBRAIN_RETICULAR_N = 'MRN - Midbrain reticular nucleus'
    S_CM__SUPERIOR_COLLICULUS = 'SCm - Superior colliculus motor related'
    PAG__PERIAQUEDUCTAL_GRAY = 'PAG - Periaqueductal gray'
    APN__ANTERIOR_PRETECTAL_N = 'APN - Anterior pretectal nucleus'
    MPT__MEDIAL_PRETECTAL_ARE = 'MPT - Medial pretectal area'
    NOT__NUCLEUS_OF_THE_OPTIC = 'NOT - Nucleus of the optic tract'
    NPC__NUCLEUS_OF_THE_POSTE = 'NPC - Nucleus of the posterior commissure'
    OP__OLIVARY_PRETECTAL_NUC = 'OP - Olivary pretectal nucleus'
    PPT__POSTERIOR_PRETECTAL = 'PPT - Posterior pretectal nucleus'
    RPF__RETROPARAFASCICULAR = 'RPF - Retroparafascicular nucleus'
    CUN__CUNEIFORM_NUCLEUS = 'CUN - Cuneiform nucleus'
    RN__RED_NUCLEUS = 'RN - Red nucleus'
    III__OCULOMOTOR_NUCLEUS = 'III - Oculomotor nucleus'
    MA3__MEDIAL_ACCESORY_OCUL = 'MA3 - Medial accesory oculomotor nucleus'
    EW__EDINGER__WESTPHAL_NUC = 'EW - Edinger-Westphal nucleus'
    IV__TROCHLEAR_NUCLEUS = 'IV - Trochlear nucleus'
    PA4__PARATROCHLEAR_NUCLEU = 'Pa4 - Paratrochlear nucleus'
    VTN__VENTRAL_TEGMENTAL_NU = 'VTN - Ventral tegmental nucleus'
    AT__ANTERIOR_TEGMENTAL_NU = 'AT - Anterior tegmental nucleus'
    LT__LATERAL_TERMINAL_NUCL = 'LT - Lateral terminal nucleus of the accessory optic tract'
    DT__DORSAL_TERMINAL_NUCLE = 'DT - Dorsal terminal nucleus of the accessory optic tract'
    MT__MEDIAL_TERMINAL_NUCLE = 'MT - Medial terminal nucleus of the accessory optic tract'
    S_NC__SUBSTANTIA_NIGRA_CO = 'SNc - Substantia nigra compact part'
    PPN__PEDUNCULOPONTINE_NUC = 'PPN - Pedunculopontine nucleus'
    IF__INTERFASCICULAR_NUCLE = 'IF - Interfascicular nucleus raphe'
    IPN__INTERPEDUNCULAR_NUCL = 'IPN - Interpeduncular nucleus'
    RL__ROSTRAL_LINEAR_NUCLEU = 'RL - Rostral linear nucleus raphe'
    CLI__CENTRAL_LINEAR_NUCLE = 'CLI - Central linear nucleus raphe'
    DR__DORSAL_NUCLEUS_RAPHE = 'DR - Dorsal nucleus raphe'
    NLL__NUCLEUS_OF_THE_LATER = 'NLL - Nucleus of the lateral lemniscus'
    PSV__PRINCIPAL_SENSORY_NU = 'PSV - Principal sensory nucleus of the trigeminal'
    PB__PARABRACHIAL_NUCLEUS = 'PB - Parabrachial nucleus'
    SOC__SUPERIOR_OLIVARY_COM = 'SOC - Superior olivary complex'
    B__BARRINGTON_S_NUCLEUS = 'B - Barrington\'s nucleus'
    DTN__DORSAL_TEGMENTAL_NUC = 'DTN - Dorsal tegmental nucleus'
    PD_TG__POSTERODORSAL_TEGM = 'PDTg - Posterodorsal tegmental nucleus'
    PCG__PONTINE_CENTRAL_GRAY = 'PCG - Pontine central gray'
    PG__PONTINE_GRAY = 'PG - Pontine gray'
    PR_NC__PONTINE_RETICULAR = 'PRNc - Pontine reticular nucleus caudal part'
    SG__SUPRAGENUAL_NUCLEUS = 'SG - Supragenual nucleus'
    SUT__SUPRATRIGEMINAL_NUCL = 'SUT - Supratrigeminal nucleus'
    TRN__TEGMENTAL_RETICULAR = 'TRN - Tegmental reticular nucleus'
    V__MOTOR_NUCLEUS_OF_TRIGE = 'V - Motor nucleus of trigeminal'
    P5__PERITRIGEMINAL_ZONE = 'P5 - Peritrigeminal zone'
    ACS5__ACCESSORY_TRIGEMINA = 'Acs5 - Accessory trigeminal nucleus'
    PC5__PARVICELLULAR_MOTOR = 'PC5 - Parvicellular motor 5 nucleus'
    I5__INTERTRIGEMINAL_NUCLE = 'I5 - Intertrigeminal nucleus'
    CS__SUPERIOR_CENTRAL_NUCL = 'CS - Superior central nucleus raphe'
    LC__LOCUS_CERULEUS = 'LC - Locus ceruleus'
    LDT__LATERODORSAL_TEGMENT = 'LDT - Laterodorsal tegmental nucleus'
    NI__NUCLEUS_INCERTUS = 'NI - Nucleus incertus'
    PR_NR__PONTINE_RETICULAR = 'PRNr - Pontine reticular nucleus'
    RPO__NUCLEUS_RAPHE_PONTIS = 'RPO - Nucleus raphe pontis'
    SLC__SUBCERULEUS_NUCLEUS = 'SLC - Subceruleus nucleus'
    SLD__SUBLATERODORSAL_NUCL = 'SLD - Sublaterodorsal nucleus'
    MY__MEDULLA = 'MY - Medulla'
    AP__AREA_POSTREMA = 'AP - Area postrema'
    DCO__DORSAL_COCHLEAR_NUCL = 'DCO - Dorsal cochlear nucleus'
    VCO__VENTRAL_COCHLEAR_NUC = 'VCO - Ventral cochlear nucleus'
    CU__CUNEATE_NUCLEUS = 'CU - Cuneate nucleus'
    GR__GRACILE_NUCLEUS = 'GR - Gracile nucleus'
    ECU__EXTERNAL_CUNEATE_NUC = 'ECU - External cuneate nucleus'
    NTB__NUCLEUS_OF_THE_TRAPE = 'NTB - Nucleus of the trapezoid body'
    NTS__NUCLEUS_OF_THE_SOLIT = 'NTS - Nucleus of the solitary tract'
    SPVC__SPINAL_NUCLEUS_OF_T = 'SPVC - Spinal nucleus of the trigeminal caudal part'
    SPVI__SPINAL_NUCLEUS_OF_T = 'SPVI - Spinal nucleus of the trigeminal interpolar part'
    SPVO__SPINAL_NUCLEUS_OF_T = 'SPVO - Spinal nucleus of the trigeminal oral part'
    PA5__PARATRIGEMINAL_NUCLE = 'Pa5 - Paratrigeminal nucleus'
    VI__ABDUCENS_NUCLEUS = 'VI - Abducens nucleus'
    VII__FACIAL_MOTOR_NUCLEUS = 'VII - Facial motor nucleus'
    AMB__NUCLEUS_AMBIGUUS = 'AMB - Nucleus ambiguus'
    DMX__DORSAL_MOTOR_NUCLEUS = 'DMX - Dorsal motor nucleus of the vagus nerve'
    GRN__GIGANTOCELLULAR_RETI = 'GRN - Gigantocellular reticular nucleus'
    ICB__INFRACEREBELLAR_NUCL = 'ICB - Infracerebellar nucleus'
    IO__INFERIOR_OLIVARY_COMP = 'IO - Inferior olivary complex'
    IRN__INTERMEDIATE_RETICUL = 'IRN - Intermediate reticular nucleus'
    ISN__INFERIOR_SALIVATORY = 'ISN - Inferior salivatory nucleus'
    LIN__LINEAR_NUCLEUS_OF_TH = 'LIN - Linear nucleus of the medulla'
    LRN__LATERAL_RETICULAR_NU = 'LRN - Lateral reticular nucleus'
    MARN__MAGNOCELLULAR_RETIC = 'MARN - Magnocellular reticular nucleus'
    MDRN__MEDULLARY_RETICULAR = 'MDRN - Medullary reticular nucleus'
    PARN__PARVICELLULAR_RETIC = 'PARN - Parvicellular reticular nucleus'
    PAS__PARASOLITARY_NUCLEUS = 'PAS - Parasolitary nucleus'
    PGRN__PARAGIGANTOCELLULAR = 'PGRN - Paragigantocellular reticular nucleus'
    NR__NUCLEUS_OF__ROLLER = 'NR - Nucleus of Roller'
    PRP__NUCLEUS_PREPOSITUS = 'PRP - Nucleus prepositus'
    PMR__PARAMEDIAN_RETICULAR = 'PMR - Paramedian reticular nucleus'
    PPY__PARAPYRAMIDAL_NUCLEU = 'PPY - Parapyramidal nucleus'
    LAV__LATERAL_VESTIBULAR_N = 'LAV - Lateral vestibular nucleus'
    MV__MEDIAL_VESTIBULAR_NUC = 'MV - Medial vestibular nucleus'
    SPIV__SPINAL_VESTIBULAR_N = 'SPIV - Spinal vestibular nucleus'
    SUV__SUPERIOR_VESTIBULAR = 'SUV - Superior vestibular nucleus'
    X__NUCLEUS_X = 'x - Nucleus x'
    XII__HYPOGLOSSAL_NUCLEUS = 'XII - Hypoglossal nucleus'
    Y__NUCLEUS_Y = 'y - Nucleus y'
    RM__NUCLEUS_RAPHE_MAGNUS = 'RM - Nucleus raphe magnus'
    RPA__NUCLEUS_RAPHE_PALLID = 'RPA - Nucleus raphe pallidus'
    RO__NUCLEUS_RAPHE_OBSCURU = 'RO - Nucleus raphe obscurus'
    LING__LINGULA_I = 'LING - Lingula (I)'
    CENT2__LOBULE_II = 'CENT2 - Lobule II'
    CENT3__LOBULE_III = 'CENT3 - Lobule III'
    CUL4_5__LOBULES_IV_V = 'CUL4 5 - Lobules IV-V'
    DEC__DECLIVE_VI = 'DEC - Declive (VI)'
    FOTU__FOLIUM_TUBER_VERMIS = 'FOTU - Folium-tuber vermis (VII)'
    PYR__PYRAMUS_VIII = 'PYR - Pyramus (VIII)'
    UVU__UVULA_IX = 'UVU - Uvula (IX)'
    NOD__NODULUS_X = 'NOD - Nodulus (X)'
    SIM__SIMPLE_LOBULE = 'SIM - Simple lobule'
    A_NCR1__CRUS_1 = 'ANcr1 - Crus 1'
    A_NCR2__CRUS_2 = 'ANcr2 - Crus 2'
    PRM__PARAMEDIAN_LOBULE = 'PRM - Paramedian lobule'
    COPY__COPULA_PYRAMIDIS = 'COPY - Copula pyramidis'
    PFL__PARAFLOCCULUS = 'PFL - Paraflocculus'
    FL__FLOCCULUS = 'FL - Flocculus'
    FN__FASTIGIAL_NUCLEUS = 'FN - Fastigial nucleus'
    IP__INTERPOSED_NUCLEUS = 'IP - Interposed nucleus'
    DN__DENTATE_NUCLEUS = 'DN - Dentate nucleus'
    VE_CB__VESTIBULOCEREBELLA = 'VeCB - Vestibulocerebellar nucleus'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NSB2023Burr6IntendedCcfTarget from a JSON string"""
        return cls(json.loads(json_str))


