---------------- 34662936 kmahadeviah (ends in 6 weeks, 1 day) ----------------
   start: 2019-05-21 10:23:49 EDT       prio: 0 type: NORMAL
     end: 2019-07-30 00:40:00 EDT       (active)
    desc: LAB-4451 - Perf PRE+SPM SPC2000 rig#2
Reservation 34662936 contains the following resources:
  *Type*  *DNS*              *Name*  *Role*
  svlg.1  TSW-D1-37              c1  svlg
  svlg.2  TSW-G18-27             c2  svlg
  svlg.3  TSW-C3-07              c3  svlg
  svlg.4  TSW-C3-10              c4  svlg
  tpc.1   TPC-D11-05-001       pre1  pre-kvm
  tpc.2   TPC-D11-10-002       pre2  pre-kvm
  tpc.3   TPC-D11-10-001       pre3  pre-kvm
  tpc.4   TPC-D11-05-002       pre4  pre-kvm
  svlg.5  TSW-C3-09              s1  svlg
  svlg.6  TSW-G18-28             s2  svlg
  svlg.7  TSW-D1-38              s3  svlg
  svlg.8  TSW-D10-07             s4  svlg
  tpc.5   TPC-D7-09-013   sde1-pcrf  sdevpl-kvm
  tpc.6   TPC-D12-19-003       spm1  mpe-kvm
  tpc.7   TPC-D12-19-004       spm2  mpe-kvm

  
  
  
define "MCC_LENGTH"                                     = 3
define "GY_RADIUS_3GPP_SGSN_MCC_SUBCONTEXT_LATEST"      = Left(Session.AttributeView.Data.X3GPP_SGSN_MCC_MNC, MCC_LENGTH)
define "GY_RADIUS_3GPP_SGSN_MNC_SUBCONTEXT_LATEST"      = SubStr(Session.AttributeView.Data.X3GPP_SGSN_MCC_MNC, MCC_LENGTH)


PolicGroup
{
 if expr(Session.IsEnd)
 
 
 PolicyGroup expr(Session.ISEnd) all
{
// Lookup into the  table using IpAddress
// Get Rx and Tx Bytes
Werite to logging UDR
delete the table row
}
delete_row <cursorname?






PolicyGroup expr(Session.ISEnd) all
{
// Lookup into the  table using IpAddress
// Get Rx and Tx Bytes
Werite to logging UDR
delete the table row
}
delete_row <cursorname?
1) Testw with only Session.IsEnd
2) add a timer column to this table
arm that timer on Session.IsNEw to 120 seconds
On Session.IsEnd or
Table.tab;lename.timercolumnname.expired
and rearm the timer
per sessionid and per rating group









From Gangaraju KS to Everyone:  06:45 PM
PolicyGroup expr(Session.ISEnd) all
{
// Lookup into the  table using IpAddress
// Get Rx and Tx Bytes
Werite to logging UDR
delete the table row
}
delete_row <cursorname?
1) Testw with only Session.IsEnd
2) add a timer column to this table
arm that timer on Session.IsNEw to 120 seconds
On Session.IsEnd or
Table.tab;lename.timercolumnname.expired
and rearm the timer
per sessionid and per rating group
