nos = ['rua1', 'rua2', 'rua3', 'rua4', 'rua5', 'rua6', 'rua7', 'rua8', 'rua9', 'rua10', 'rua11', 'rua12', 
       'rua13', 'rua14', 'rua15', 'rua16', 'rua17', 'rua18', 'rua19', 'rua20', 'rua21', 'rua22', 'rua23', 
       'rua24', 'rua25', 'rua26', 'rua27', 'rua28', 'rua29', 'rua30', 'rua31', 'rua32', 'rua33', 'rua34', 
       'rua35', 'rua36', 'rua37', 'rua38', 'rua39', 'rua40', 'rua41', 'rua42', 'rua43','avenidaA','avenidaB',
       'avenidaC','avenidaD','avenidaE','avenidaF','cruzamentoA','cruzamentoB','viaA','viaB','rotatoriaA']


grafo = [[['rua2',2],['rua3',2],['rua4',3],['rua5',3],['rua6',3],['rua7',3],['rua10',4],['rua9',5]],
         [['avenidaF',1],['rua1',1]],
         [['rua1',1],['avenidaB'],1],
         [['avenidaF',1],['rua1',1]],
         [['rua1',1],['avenidaB',1]],
         [['avenidaF',1],['rua1',1]],
         [['rua1',1],['avenidaB',1],['rua8',2]],
         [['rua7',1],['rua9',2]],
         [['avenidaF',1],['cruzamentoB',2],['rua8',3]],
         [['avenidaF',1],['rua1',1]],
         [['rua13',3],['avenidaF',1]],
         [['rua13',1],['avenidaF',1]],
         [['rua12',4],['rua11',5]],[['viaA',3],['avenidaA',1]],
         [['viaA',1],['viaB',1]],
         [['rua22',1],['rua19',6],['rua20',7],['viaB',8]],
         [['rua22',1],['rua17',3],['rua18',4],['rua19',5]],
         [['rua23',3],['rua16',1]],
         [['rua16',1],['rua21',3],['rotatoriaA',4]],
         [['rua21',3],['rua26',4],['rua16',2],['rua15',1]],
         [['rua15',1],['rua21',4],['rua26',6]],
         [['rua18',1],['rua19',2],['rua20',3]],
         [['rua23',1],['rua16',5],['rua15',6],['rua24',8]],
         [['rua22',1],['rua17',2],['rotatoriaA',1]],
         [['rua22',1],['avenidaA',5]],
         [['rotatoriaA',1],['avenidaC',3]],
         [['rotatoriaA',1],['rua19',1],['rua20',2],['avenidaC',4]],
         [['rotatoriaA',1],['avenidaC',2],['avenidaD',3],['avenidaE',5]],
         [['avenidaD',1],['avenidaE',1]],
         [['avenidaE',1],['rua30',2]],
         [['rua29',1],['rua32',1]],
         [['avenidaC',1],['avenidaD',1]],
         [['avenidaD',1],['avenidaE',1],['rua30',2]],
         [['rua32',1],['rua35',1],['avenidaF'],7],
         [['avenidaC',1],['avenidaD',1]],
         [['avenidaD',1],['avenidaE',1],['rua33',3]],
         [['avenidaF',1],['rua41',3]],
         [['avenidaF',1],['rua40',2]],
         [['avenidaF',1],['cruzamentoB',1],['rua43',6]],
         [['rua36',1],['rua42',1]],
         [['rua38',1],['rua37',1]],
         [['rua36',1],['rua37',1]],
         [['avenidaF',1],['rua41',2],['rua43',3]],
         [['avenidaB',1],['rua37',1],['rua36',3],['rua42',3]],
         [['rua24',1],['cruzamentoA',2],['rua13',2],['rua1',5],['avenidaB',8]],
         [['avenidaA',1],['rua3',1],['rua5',2],['rua7',3],['rua43',10]],
         [['rua27',1],['rua25',2],['rua26',3],['viaB',3],['viaA',7],['rua31',7],['rua34',8]],
         [['rua27',1],['rua28',4],['rua32',5],['rua35',6],['avenidaF',10]],
         [['rua27',1],['rua28',2],['rua29',2],['rua32',3],['rua34',5],['avenidaF',12]],
         [['rua2',1],['rua4',2],['rua6',3],['rua10',4],['rua12',4],['rua11',5],['rua9',5],['rua38',7],['rua37',8],['rua36',9],['rua37',10]],
         [['viaB',1],['avenidaA',3],['rua9',1],['rua38',1]],
         [['avenidaC',1],['rua14',6],['rua13',9]],
         [['rua26',1],['avenidaC',1],['rua14',6]],
         [['rua23',1],['rua18',2],['rua26',3],['rua25',2],['rua27',3]]
]    