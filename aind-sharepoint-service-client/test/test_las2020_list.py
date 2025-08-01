# coding: utf-8

"""
    aind-sharepoint-service

     ## aind-sharepoint-service  Service to pull data from Sharepoint.  

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from aind_sharepoint_service_client.models.las2020_list import Las2020List

class TestLas2020List(unittest.TestCase):
    """Las2020List unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Las2020List:
        """Test Las2020List
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Las2020List`
        """
        model = Las2020List()
        if include_optional:
            return Las2020List(
                accommodation_comment = '',
                acsf_time1 = '',
                acsf_time2 = '',
                acsf_time3 = '',
                acsf_time4 = '',
                acsf_time5 = '',
                acsfid1 = '',
                acsfid2 = '',
                acsfid3 = '',
                acsfid4 = '',
                acsfid5 = '',
                afternoon_pf = True,
                author_id = 56,
                author_lookup_id = 56,
                bc_age = '',
                bc_genotypes = '',
                bc_location = '',
                bc_tube = '',
                bc_type = 'Submandibular',
                bc_volume = '',
                color_tag = '',
                compliance_asset_id = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                custcontact = '',
                custom_com1 = '',
                custom_com2 = '',
                custpresent = True,
                dose_route = 'Intramuscular (IM)',
                dose_sub = '',
                dose_where = '',
                doseduration = '',
                dosevolume = '',
                doxycycline = True,
                editor_id = 56,
                icv_comment = '',
                icv_id1 = '',
                icv_id2 = '',
                icv_id3 = '',
                icv_id4 = '',
                icv_id5 = '',
                icv_lims = 'New Stereotaxic Injections',
                icv_route1 = 'Any, Unilateral',
                icv_route2 = 'Any, Unilateral',
                icv_route3 = 'Any, Unilateral',
                icv_route4 = 'Any, Unilateral',
                icv_route5 = 'Any, Unilateral',
                icv_sub1 = '',
                icv_sub2 = '',
                icv_sub3 = '',
                icv_sub4 = '',
                icv_sub5 = '',
                id = 56,
                lta_id1 = '',
                lta_id2 = '',
                lta_id3 = '',
                lta_id4 = '',
                lta_id5 = '',
                l_tdate1 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                l_tdate2 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                l_tdate3 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                l_tdate4 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                l_tdate5 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                las_comments = '',
                lims_entry = True,
                lims_project = 'aind-discovery',
                lims_workflow = 'Characterization',
                lims_workflow_x0020_2 = 'Characterization',
                lt_task1 = '',
                lt_task2 = '',
                lt_task3 = '',
                lt_task4 = '',
                lt_task5 = '',
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                n_end_x0020_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                n_roid1 = '',
                n_roid2 = '',
                n_roid3 = '',
                n_roid4 = '',
                n_roid5 = '',
                n_start_x0020_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                oct = True,
                post_fix = 'Nuclease-free 1xPBS (omFISH)',
                project_id = 'AAV production 102-88-004-10',
                protocol = '2103 - Optical Physiology Mindscope Phase 4',
                qc_door_sheet = True,
                req_age1 = '',
                req_age2 = '',
                req_age3 = '',
                req_pro1 = 'Blood Collection',
                req_pro2 = 'Blood Collection',
                req_pro3 = 'Blood Collection',
                reqdate1 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reqdate2 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reqdate3 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                request_status2 = 'Cancelled',
                ro_box1 = '',
                ro_box2 = '',
                ro_box3 = '',
                ro_box4 = '',
                ro_box5 = '',
                ro_comment = '',
                ro_discard = True,
                ro_eye1 = 'Behind Either',
                ro_eye2 = 'Behind Either',
                ro_eye3 = 'Behind Either',
                ro_eye4 = 'Behind Either',
                ro_eye5 = 'Behind Either',
                ro_gc1 = '',
                ro_gc1b = '',
                ro_gc1c = '',
                ro_gc1d = '',
                ro_gc2 = '',
                ro_gc2b = '',
                ro_gc2c = '',
                ro_gc2d = '',
                ro_gc3 = '',
                ro_gc3b = '',
                ro_gc3c = '',
                ro_gc3d = '',
                ro_gc4 = '',
                ro_gc4b = '',
                ro_gc4c = '',
                ro_gc4d = '',
                ro_gc5 = '',
                ro_gc5b = '',
                ro_gc5c = '',
                ro_gc5d = '',
                ro_ice = True,
                ro_lims = 'New Stereotaxic Injections',
                ro_lot1 = '',
                ro_lot1b = '',
                ro_lot1c = '',
                ro_lot1d = '',
                ro_lot2 = '',
                ro_lot2b = '',
                ro_lot2c = '',
                ro_lot2d = '',
                ro_lot3 = '',
                ro_lot3b = '',
                ro_lot3c = '',
                ro_lot3d = '',
                ro_lot4 = '',
                ro_lot4b = '',
                ro_lot4c = '',
                ro_lot4d = '',
                ro_lot5 = '',
                ro_lot5b = '',
                ro_lot5c = '',
                ro_lot5d = '',
                ro_sop = 'AF0131 Retro-orbital Injection',
                ro_spin_down = True,
                ro_sub1 = '',
                ro_sub1b = '',
                ro_sub1c = '',
                ro_sub1d = '',
                ro_sub2 = '',
                ro_sub2b = '',
                ro_sub2c = '',
                ro_sub2d = '',
                ro_sub3 = '',
                ro_sub3b = '',
                ro_sub3c = '',
                ro_sub3d = '',
                ro_sub4 = '',
                ro_sub4b = '',
                ro_sub4c = '',
                ro_sub4d = '',
                ro_sub5 = '',
                ro_sub5b = '',
                ro_sub5c = '',
                ro_sub5d = '',
                ro_tite1 = '',
                ro_tite1b = '',
                ro_tite1c = '',
                ro_tite1d = '',
                ro_tite2 = '',
                ro_tite2b = '',
                ro_tite2c = '',
                ro_tite2d = '',
                ro_tite3 = '',
                ro_tite3b = '',
                ro_tite3c = '',
                ro_tite3d = '',
                ro_tite4 = '',
                ro_tite4b = '',
                ro_tite4c = '',
                ro_tite4d = '',
                ro_tite5 = '',
                ro_tite5b = '',
                ro_tite5c = '',
                ro_tite5d = '',
                ro_tube1 = '',
                ro_tube2 = '',
                ro_tube3 = '',
                ro_tube4 = '',
                ro_tube5 = '',
                ro_vol1 = '',
                ro_vol2 = '',
                ro_vol3 = '',
                ro_vol4 = '',
                ro_vol5 = '',
                ro_vol_v1 = '',
                ro_vol_v1b = '',
                ro_vol_v1c = '',
                ro_vol_v1d = '',
                ro_vol_v2 = '',
                ro_vol_v2b = '',
                ro_vol_v2c = '',
                ro_vol_v2d = '',
                ro_vol_v3 = '',
                ro_vol_v3b = '',
                ro_vol_v3c = '',
                ro_vol_v3d = '',
                ro_vol_v4 = '',
                ro_vol_v4b = '',
                ro_vol_v4c = '',
                ro_vol_v4d = '',
                ro_vol_v5 = '',
                ro_vol_v5b = '',
                ro_vol_v5c = '',
                ro_vol_v5d = '',
                ro_where = 'LAS blue bin in Vivarium -80 freezer(1st shelf)',
                spec_deli_loc = '',
                species = 'Mouse',
                tam = True,
                tam_age = '',
                tam_freq = 'Other (Type in)',
                title = '',
                tmp = True,
                tmp_age = '',
                tmp_freq = 'Other (Type-in)',
                ui_version_string = '',
                wellness_report_x0028_no_x002_f_ye = True,
                whereto_obtainsubstance_x0028_icv = 'LAS blue bin in Vivarium –80 freezer'
            )
        else:
            return Las2020List(
        )
        """

    def testLas2020List(self):
        """Test Las2020List"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
