#!/usr/bin/env python

from p2pool import main

_zen_version = 4.0313
ascii_out = '''
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                      ...                                                           
                                                                   0pp00000       .000000.    .00.                                  
                            .0ppppp00      0ppppp0     0pppppp0.                        .0   .22P.                                  
                            p22PppP22P0   P2PppP22P   .22PppP222p                            p220                                   
                           .222.   p22P   ..   .22P   p22p   .222.  .pPPPPp0     0pPPPPp.   .22P                                    
                           p22P  .0P220      .pP2P.  .222. ..p22P  p22p00P22p  0P2Pp0pP2P.  p220                                    
                          .P2222222Pp0     0P2Pp0    p22222222P0  p22p   022P .22P.   p220 .22P.                                    
                          p22P000..     .pP2P0      .22P000..    .P22.   p22p 022p   .P2P. p22p                                     
                         .P220         0P22P00000.  p22p          P22p00P22p  022P00pP2P0  P22p.                                    
                         0PPp          pPPPPPPPPp. .pPP.           0pPPPpp.    .pPPPPp0    .pPP0                                    
                                                                                        ..                                          
                                                                 0Pp0.              .0pPP                                           
                                                                  .Pp0pPpp0.....0pPP0.0P.                                           
                             Decentralized Mining Pool Node         pp.pP22222222PP0.pp                                             
                                                                     .p0 ..0000..  0p0                                              
                             this node is running                      0pp0.    .0p0                                                
                                                                          00000p0.                                                  
                              ZEN2pool v%s                                                                                          
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
''' % (_zen_version)
print ascii_out

main.run()
