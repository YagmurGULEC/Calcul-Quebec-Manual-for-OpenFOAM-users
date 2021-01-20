import paraview.simple as pvs
case_foam = pvs.OpenFOAMReader( FileName='./case.foam' )
case_foam.CaseType = 'Decomposed Case'
case_foam.CellArrays = ['ContactLineField', 'H', 'T', 'U', 'WallField', 'alpha1', 'cellStatus', 'interfaceArea_iso', 'p', 'p_rgh']
case_foam.MeshRegions = ['internalMesh']

IsoVolume1 = pvs.IsoVolume()
IsoVolume1.ThresholdRange = [0.5, 0.51]
IsoVolume1.InputScalars = ['POINTS', 'alpha1']
writer=pvs.CreateWriter('./interface.csv', proxy=IsoVolume1)
writer.FieldAssociation = "Points"
writer.WriteAllTimeSteps=1
writer.UpdatePipeline()
