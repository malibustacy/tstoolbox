
import pandas as pd

# Monthly time-series starting in May, 1874
values = [
 365.1,
 415.2,
1033.5,
 954.1,
 335.3,
 515.0,
 465.4,
 192.5,
  89.8,
 399.2,
 423.0,
 393.8,
 145.4,
 454.0,
  76.8,
 124.2,
  34.0,
 132.4,
 194.0,
  91.0,
 167.5,
 263.6,
 231.4,
  15.8,
  37.3,
  15.2,
  67.8,
  34.7,
 104.4,
 155.3,
  69.1,
 149.3,
 188.9,
  66.2,
  65.7,
  93.8,
  85.5,
  69.0,
   4.2,
  34.9,
  73.0,
 126.3,
 283.5,
  23.3,
  14.9,
  18.1,
  47.9,
   0.4,
  51.5,
  41.0,
   0.4,
   0.0,
  57.2,
   9.6,
  23.6,
   2.0,
   1.2,
   0.0,
   0.0,
  50.5,
   5.8,
  19.6,
  51.4,
  38.5,
  41.3,
  81.5,
 112.4,
  33.8,
 292.2,
 337.6,
 142.7,
 232.2,
 409.0,
 488.2,
 206.1,
 821.3,
 926.5,
 561.5,
 483.1,
 460.6,
 585.2,
 675.9,
 640.5,
 530.2,
 376.9,
 612.4,
 941.1,
 738.0,
 867.0,
 705.1,
 840.4,
 641.2,
 364.0,
 673.1,
 928.9,
1799.1,
1519.6,
 557.8,
 461.5,
 607.6,
1026.9,
1393.8,
1931.1,
 352.9,
 849.8,
 734.8,
 621.2,
1132.5,
 339.4,
1451.4,
2007.7,
 595.6,
1230.2,
1793.3,
1725.6,
1305.4,
1669.7,
1536.9,
1207.3,
1581.2,
1210.8,
 501.6,
 561.3,
 727.1,
1115.1,
 994.5,
 438.0,
 866.0,
 512.0,
1083.1,
 747.0,
 855.4,
1059.0,
1702.4,
1155.4,
 598.0,
 646.0,
 718.5,
 425.2,
 220.5,
 544.5,
 312.9,
1032.2,
 623.6,
 688.4,
 398.1,
 395.4,
 115.4,
 193.6,
  57.5,
   1.6,
 189.7,
  79.7,
  75.6,
  30.5,
  44.8,
 252.7,
 302.1,
 370.5,
 162.9,
 121.8,
  54.0,
  52.3,
 580.2,
 117.4,
  91.4,
  88.2,
  26.0,
 185.6,
  32.5,
  22.2,
  65.3,
  98.7,
  10.5,
 240.3,
  77.0,
   2.4,
  27.9,
  27.8,
  26.9,
  14.4,
 217.2,
 153.5,
 282.3,
  89.9,
  11.6,
   0.0,
  66.4,
  42.3,
   1.4,
  69.5,
   8.9,
  21.8,
   9.3,
 139.8,
 157.6,
 229.0,
 245.6,
 181.5,
  78.5,
 211.7,
 266.7,
 158.7,
 354.4,
 553.4,
 594.5,
1021.9,
 550.7,
1301.4,
 605.3,
 637.4,
 541.2,
1252.7,
1788.1,
 757.8,
 994.3,
1541.8,
1117.7,
1920.7,
1429.5,
1002.7,
 910.9,
 953.6,
 865.5,
1158.1,
1283.8,
 962.9,
1178.4,
1161.8,
1379.0,
1573.8,
2340.8,
1644.5,
1504.0,
1312.7,
2027.7,
1564.7,
1486.2,
 623.5,
1603.6,
1779.1,
1898.4,
1740.6,
1164.5,
 666.2,
1227.8,
 585.4,
1038.5,
 942.0,
 937.1,
1018.0,
1074.5,
 901.8,
1143.5,
 465.2,
1376.0,
 831.7,
1231.8,
 722.5,
1037.1,
 285.0,
 900.0,
 543.6,
 423.5,
 181.1,
 820.6,
 513.4,
 273.6,
1182.6,
 303.6,
 608.6,
 533.1,
1331.0,
 912.6,
 523.8,
 384.1,
 398.3,
 217.5,
 308.7,
 492.7,
 703.9,
  82.7,
  34.2,
 750.3,
 411.0,
 524.0,
 624.5,
 159.1,
 247.5,
  64.8,
  48.1,
 463.8,
 858.2,
 605.5,
 317.4,
 172.0,
 215.6,
  40.1,
 280.6,
 143.7,
  50.7,
 203.3,
 197.1,
   1.4,
  25.4,
  74.8,
  32.9,
  54.2,
  56.5,
 109.9,
 151.5,
  97.4,
 127.6,
 113.7,
  51.5,
  10.7,
  23.1,
 138.2,
  11.6,
   0.0,
   0.2,
   6.4,
  13.3,
   0.0,
 208.5,
  41.6,
   1.0,
   0.0,
   0.2,
  14.8,
  48.3,
   0.0,
  98.3,
   0.4,
 179.8,
   0.0,
  36.1,
   5.9,
   0.3,
   2.4,
  76.0,
 161.4,
 149.6,
   3.5,
  30.0,
 129.9,
 189.8,
 336.3,
  84.1,
 105.9,
 277.3,
 112.8,
  84.4,
1204.7,
 911.3,
 596.7,
 411.7,
 345.4,
 375.8,
 901.3,
 268.1,
 330.4,
 511.3,
 576.2,
 254.6,
 634.9,
 470.5,
 777.9,
1100.6,
1983.4,
1297.7,
 408.4,
 667.6,
 651.4,
1585.3,
1159.5,
 696.2,
2060.5,
1946.3,
 793.7,
 736.5,
 395.1,
1057.4,
 687.9,
1105.5,
 749.3,
1446.9,
 738.5,
 516.3,
  98.7,
 560.7,
1207.0,
1196.7,
2453.0,
 809.0,
 700.9,
 608.3,
 949.4,
 882.5,
 824.5,
1410.2,
1193.4,
1074.6,
1002.8,
 507.2,
 270.4,
 217.9,
 707.3,
 508.7,
 630.8,
 350.8,
1750.4,
1701.4,
 369.3,
 717.5,
 638.1,
1192.5,
 774.4,
1026.5,
 470.9,
 503.1,
 282.7,
 563.5,
 128.9,
 801.6,
 866.9,
 794.0,
 893.3,
 381.8,
 632.8,
 287.4,
  70.0,
 326.8,
 118.3,
 186.5,
 181.7,
 434.4,
 511.7,
  23.7,
  37.0,
  39.3,
  88.5,
  70.5,
 260.0,
 101.8,
  30.0,
  11.5,
  27.6,
  53.1,
  17.9,
  57.2,
  15.5,
   0.0,
   0.0,
  57.4,
  88.2,
  21.4,
  84.4,
   9.5,
   0.3,
  47.3,
  55.0,
   2.9,
  81.6,
  14.8,
  23.2,
   0.8,
   3.3,
   0.0,
   0.0,
   6.8,
   0.0,
   3.6,
  14.8,
   5.2,
  17.8,
  13.0,
  10.7,
  38.7,
 286.8,
  69.9,
 172.5,
  46.7,
 296.7,
 344.0,
  33.1,
 222.0,
 294.5,
 302.5,
 670.6,
 483.1,
 964.9,
 528.3,
 969.0,
1307.9,
 946.2,
 750.0,
 647.3,
 444.9,
 358.5,
 509.6,
 712.6,
 950.9,
 806.4,
1037.8,
1156.9,
 572.5,
 338.9,
 466.2,
 722.0,
 637.5,
 794.2,
1045.8,
1415.4,
1152.9,
 919.7,
1445.9,
1717.2,
1554.0,
2977.7,
1875.0,
 978.5,
1027.9,
2297.1,
1797.4,
 800.4,
 854.2,
 979.4,
 953.3,
 567.5,
1281.5,
1805.1,
 944.4,
1229.1,
1040.8,
1097.7,
 623.5,
1363.4,
1190.2,
 707.5,
1651.3,
1876.6,
 902.4,
1383.9,
1095.4,
 774.4,
 761.2,
 326.4,
1167.2,
 553.0,
1416.0,
 327.8,
 301.4,
 539.2,
 407.1,
 183.6,
 851.6,
 617.6,
 603.4,
 439.2,
 490.7,
 318.0,
 392.6,
 448.6,
 604.0,
 387.4,
 577.4,
 270.8,
 332.9,
 310.6,
 505.4,
 397.0,
  90.5,
 493.0,
1235.9,
  85.4,
 123.8,
  16.1,
 116.8,
  86.6,
  57.5,
  63.5,
 176.3,
 478.1,
  93.5,
   1.8,
  16.0,
  30.4,
  19.5,
  73.6,
  29.3,
   1.7,
 134.4,
 117.2,
 112.7,
  25.8,
   1.7,
  68.0,
  33.3,
 148.5,
 246.8,
 427.0,
 358.5,
 360.3,
 422.8,
 468.5,
 608.4,
 192.3,
  36.2,
 313.6,
 231.0,
 311.8,
 703.2,
 648.3,
 426.1,
 473.7,
 759.7,
1304.9,
1432.5,
3259.9,
2695.0,
1915.8,
1272.8,
 469.0,
1085.9,
1277.2,
 842.5,
 874.5,
1216.3,
1418.6,
 650.3,
1439.9,
1810.0,
1364.8,
 902.3,
1379.0,
 967.3,
 873.6,
 811.8,
1030.1,
1173.1,
 819.3,
 975.2,
 623.1,
1509.2,
1146.2,
1694.3,
1368.1,
1243.1,
1358.9,
1936.4,
1331.9,
2213.5,
 992.5,
 794.4,
1078.5,
 980.1,
 821.6,
1058.0,
1037.0,
 849.4,
1199.0,
1026.9,
 744.0,
 278.0,
1309.9,
2478.8,
3084.3,
1141.3,
 683.7,
 656.7,
 561.5,
 490.3,
 278.7,
 152.9,
 283.1,
 368.2,
 682.3,
 661.3,
 239.3,
 179.7,
 812.1,
 552.6,
 431.8,
 291.6,
 178.5,
 108.6,
  82.9,
 149.1,
  94.5,
 263.2,
 204.2,
 127.1,
 123.5,
 150.4,
 222.5,
 323.0,
 344.0,
 116.1,
  79.9,
   8.6,
  71.0,
 125.2,
 266.5,
 179.8,
 608.5,
 162.3,
  15.4,
  15.7,
  39.0,
  12.2,
   0.3,
  19.5,
  37.3,
   4.3,
   0.7,
  42.8,
  58.9,
  11.4,
 355.0,
 373.4,
  99.7,
 105.9,
  96.5,
  21.1,
  21.1,
  79.9,
 153.0,
 312.2,
 256.1,
 196.9,
 126.2,
 361.8,
 690.2,
 571.8,
 444.5,
 544.7,
 741.4,
1557.1,
1662.0,
1647.4,
1226.7,
1128.0,
1044.6,
 566.0,
 804.2,
 628.8,
 952.0,
 924.1,
1084.8,
1938.1,
1745.4,
2252.9,
2347.5,
1142.9,
2256.6,
2337.3,
2712.5,
3363.4,
2504.1,
1504.5,
2358.4,
 852.8,
1240.4,
2264.8,
1744.0,
1473.5,
2365.6,
2319.7,
1322.8,
3163.3,
1678.7,
1603.4,
1917.3,
2412.9,
1916.8,
1159.1,
1031.2,
 763.2,
1999.7,
1751.0,
1130.6,
1962.4,
2326.9,
3165.1,
1920.3,
1170.6,
 541.9,
1158.5,
 963.7,
1467.5,
 642.1,
 668.3,
1297.0,
 893.1,
1899.8,
 945.8,
1057.6,
 594.3,
 858.3,
 483.9,
 478.9,
 519.5,
 347.3,
 206.5,
 775.8,
 997.1,
 907.8,
1347.8,
 828.7,
 641.7,
 362.5,
 361.8,
 991.3,
 923.6,
 977.6,
 275.5,
  89.5,
 188.0,
 242.4,
 108.7,
 230.9,
 485.4,
 253.3,
  72.3,
 551.6,
 628.0,
 753.2,
 248.6,
  36.7,
 240.0,
 142.7,
 242.0,
 234.7,
 126.8,
 284.6,
  25.6,
   1.6,
 145.3,
   0.7,
   8.8,
  52.5,
  24.2,
  78.4,
 250.1,
 192.8,
 177.5,
 538.3,
 182.3,
  92.2,
 514.6,
 584.6,
 283.0,
 399.2,
 505.6,
 270.7,
 450.7,
1111.2,
 398.6,
 325.3,
1237.5,
3091.0,
1550.9,
1433.5,
1084.9,
 715.7,
2912.4,
2290.7,
1859.8,
1344.5,
1852.4,
2513.5,
2307.6,
2721.0,
3595.8,
3950.3,
3741.3,
1933.8,
2451.1,
3207.3,
1991.6,
2379.8,
1686.4,
1642.6,
1113.1,
1089.6,
1261.3,
3432.1,
3305.2,
2559.4,
1766.0,
2075.3,
1864.9,
1745.3,
1006.1,
2476.9,
2240.0,
3640.3,
3276.7,
1882.3,
1217.1,
1606.4,
1752.0,
2265.1,
2185.5,
1815.0,
2313.0,
1486.5,
1416.2,
1927.3,
1660.3,
2359.1,
1578.1,
1048.3,
1255.7,
1068.5,
 488.4,
 571.1,
 744.9,
 610.2,
 746.4,
 626.7,
 845.2,
1599.0,
2899.0,
2477.1,
 779.9,
 664.0,
 959.9,
 757.4,
 666.0,
 602.5,
 464.0,
 305.4,
 141.9,
 351.0,
 256.6,
 393.1,
 654.3,
 688.7,
 307.0,
 339.5,
 455.4,
 477.3,
 288.7,
  10.5,
  70.3,
 405.5,
 195.6,
 217.8,
  80.7,
 268.9,
 141.1,
  47.0,
   9.1,
   6.0,
   0.7,
   1.4,
 157.4,
   3.2,
   0.8,
   1.8,
  10.5,
  58.0,
   2.2,
  15.7,
  57.8,
 106.2,
 540.9,
 287.4,
  37.2,
  80.1,
 302.1,
 490.5,
 216.4,
 574.0,
 436.8,
 921.3,
1664.7,
1076.8,
1584.0,
2878.2,
1855.9,
1418.5,
2220.6,
1673.4,
1872.8,
3016.2,
2598.4,
2385.4,
3823.3,
3409.6,
2328.1,
1454.6,
1814.2,
2064.0,
2568.7,
4535.8,
3150.3,
2356.6,
4554.0,
4473.7,
3011.6,
4270.1,
2994.3,
2546.6,
4437.6,
3603.3,
2707.8,
2600.3,
3298.8,
2899.1,
3340.6,
2597.1,
1877.9,
3231.8,
4902.0,
2410.2,
3740.2,
2701.0,
2807.4,
3080.9,
2684.8,
3535.9,
2415.1,
1465.1,
2386.1,
2346.6,
2536.1,
1805.2,
1191.7,
1786.5,
2078.9,
1414.4,
1857.3,
2034.0,
1439.2,
1168.6,
1476.1,
 906.6,
 772.7,
 357.6,
 512.6,
 638.1,
 459.9,
 961.9,
1155.5,
 498.4,
 963.1,
 329.0,
 314.8,
 398.4,
 593.8,
 826.9,
 693.0,
 554.3,
 634.0,
 362.8,
 262.9,
 140.3,
 657.5,
 371.6,
 291.1,
 174.0,
 174.5,
 194.1,
 144.5,
 303.0,
 507.2,
 349.4,
 147.9,
 322.5,
 622.7,
 433.9,
 185.3,
  69.0,
 105.1,
  84.0,
 149.8,
  17.8,
  30.9,
  25.2,
   7.6,
  51.5,
  16.6,
  24.6,
  27.1,
 106.7,
 145.9,
 112.5,
  52.9,
  23.6,
 224.6,
  94.1,
  73.4,
  22.0,
 156.1,
 175.3,
 139.6,
 139.7,
 283.2,
 240.3,
 563.8,
 786.9,
 411.9,
 318.8,
 762.1,
 521.5,
 939.3,
 637.7,
 710.4,
 934.8,
1840.4,
1493.2,
2081.5,
 892.2,
1730.6,
1025.7,
1476.4,
2128.5,
 886.1,
1117.5,
1553.4,
2004.2,
2482.8,
1879.3,
1117.5,
1002.0,
1904.1,
1838.5,
1481.9,
1640.6,
1264.4,
1406.7,
1134.3,
1685.0,
1571.0,
1272.4,
2187.3,
1508.7,
1335.5,
1793.9,
1167.6,
1200.1,
 845.8,
1574.1,
1698.7,
1246.5,
1593.4,
2255.9,
1382.8,
1920.1,
2126.9,
1529.6,
1646.2,
1310.9,
1256.4,
1271.2,
1566.3,
1355.4,
1942.5,
1433.8,
 688.1,
 884.0,
 701.8,
 487.3,
1122.0,
1156.2,
 599.0,
 954.6,
 913.9,
 999.2,
 522.4,
1338.2,
1207.6,
 572.4,
1318.6,
1321.9,
 929.2,
1051.7,
 604.7,
1017.1,
 554.9,
 561.7,
 399.1,
 423.7,
 722.0,
 765.1,
 411.5,
 441.0,
 281.6,
 262.2,
 883.4,
 407.0,
 242.6,
 251.4,
 204.6,
 252.8,
 128.2,
 513.5,
 382.9,
 292.6,
 831.1,
 432.2,
 584.3,
 603.0,
 309.5,
 251.6,
 155.4,
  80.2,
  64.1,
  17.3,
  59.9,
 106.9,
 353.6,
 702.0,
  74.0,
 114.2,
 235.1,
  34.2,
 115.5,
  11.3,
 336.3,
 376.3,
 104.1,
  76.3,
   8.7,
 290.7,
 169.3,
 181.9,
  92.0,
 274.9,
 148.4,
 216.0,
  36.6,
 123.9,
 131.9,
 617.4,
 205.2,
 273.2,
 885.7,
 611.0,
 270.7,
 644.5,
 558.6,
1901.5,
1294.5,
1520.7,
1346.8,
1175.9,
 878.4,
 530.5,
1996.2,
1455.6,
1436.0,
2327.5,
2688.0,
2217.3,
1581.6,
1823.8,
1676.7,
2614.9,
1795.6,
2003.7,
2258.3,
2703.9,
3132.3,
1838.2,
1935.2,
2113.0,
1134.0,
2827.5,
2884.0,
1960.7,
2003.4,
1456.5,
1994.8,
2469.2,
3083.3,
2067.0,
1248.5,
2216.6,
2348.6,
2216.7,
2082.4,
1451.1,
3295.0,
1840.5,
2572.0,
3239.7,
2207.1,
2524.7,
1607.7,
3857.0,
3569.5,
2053.7,
1390.1,
3070.7,
1909.0,
2065.2,
1778.5,
1539.5,
1851.3,
2707.4,
1214.4,
 957.5,
 905.9,
 976.7,
1736.5,
1577.8,
1105.1,
 845.9,
 607.1,
 904.1,
 203.5,
 293.5,
1582.0,
2174.8,
1033.3,
1723.4,
1619.0,
 588.9,
 289.0,
 191.5,
 130.7,
  69.1,
 234.3,
  99.8,
 168.5,
 102.0,
 132.3,
 368.2,
 342.5,
 246.9,
 392.5,
  45.2,
  19.1,
 193.3,
 100.3,
  51.0,
  32.5,
 417.5,
 145.9,
 174.5,
  45.2,
   1.9,
 105.2,
  81.7,
  23.8,
 359.9,
  94.3,
  14.0,
  25.3,
  13.5,
 108.8,
 502.6,
 457.3,
 104.1,
 256.5,
 565.9,
 249.7,
 493.6,
 490.0,
 294.5,
 489.5,
 507.9,
 870.7,
1032.7,
 492.3,
1755.6,
2044.0,
1714.3,
1220.8,
2081.5,
1593.2,
2423.8,
2952.2,
2592.5,
3054.7,
1954.4,
1824.1,
3713.7,
1503.4,
3150.0,
3308.7,
2007.9,
2489.2,
2399.9,
2080.1,
1727.0,
1826.8,
1565.2,
1872.4,
1333.7,
2074.3,
3414.2,
1662.3,
1957.7,
2793.5,
2277.0,
3211.4,
3168.0,
2794.1,
1486.8,
2275.7,
2728.6,
2525.4,
2646.0,
1635.2,
2753.9,
1370.1,
3047.0,
2413.4,
2837.2,
1271.3,
1336.5,
 761.9,
 721.5,
1201.3,
1135.8,
 733.8,
1411.3,
1399.1,
 967.4,
 613.7,
1550.5,
1001.2,
 687.9,
 568.6,
 595.5,
 481.9,
 409.2,
 311.7,
 798.0,
 655.2,
 681.0,
1030.1,
 438.0,
 171.2,
 120.9,
 251.5,
 196.0,
 295.4,
 216.8,
 390.1,
 523.9,
 113.4,
 337.4,
 185.6,
 235.5,
 315.2,
 142.8,
 189.7,
 136.7,
 149.0,
  82.2,
  54.6,
 269.6,
  90.1,
  64.6,
  74.1,
  16.9,
  49.2,
  22.4,
  47.9,
  83.5,
 163.5,
 130.1,
   5.1,
   1.8,
 277.7,
 110.6,
  10.8,
  38.0,
  51.0,
  86.8,
 116.5,
  60.7,
  38.8,
 149.5,
 726.1,
 131.4,
 632.3,
 481.0,
 257.9,
 308.0,
 810.2,
 520.8,
 673.8,
 679.0,
 690.1,
1358.9,
1331.9,
 469.2,
1006.6,
1050.5,
 634.5,
 937.0,
 655.7,
 460.1,
1146.6,
1690.3,
1533.7,
1397.3,
 609.9,
1509.7,
1871.8,
1497.5,
 927.2,
1460.5,
2221.5,
1862.9,
2182.2,
2093.5,
2343.9,
1082.5,
1872.3,
 948.8,
1351.0,
1024.3,
 934.8,
 669.5,
1671.0,
1892.8,
1109.2,
1785.9,
 819.2,
1619.0,
3040.4,
2128.9,
2424.1,
2354.3,
1781.4,
1637.0,
1367.6,
2053.3,
2182.2,
1346.8,
2196.6,
2527.2,
2093.5,
1799.5,
1843.8,
1115.9,
 987.7,
 474.0,
1183.2,
1107.9,
 950.6,
1280.1,
1177.4,
 948.8,
 593.6,
2261.2,
1594.1,
 632.3,
 762.8,
 619.9,
 700.0,
 439.6,
 627.3,
 593.6,
1239.5,
 985.4,
 566.1,
 600.4,
 796.1,
 274.6,
 900.5,
 534.5,
 419.5,
 395.7,
 795.3,
 701.9,
 700.0,
 539.2,
 598.3,
  52.4,
 398.1,
 475.5,
 150.8,
  10.5,
  78.6,
 490.9,
 188.8,
 196.9,
 214.6,
 438.5,
 193.2,
  79.5,
 528.7,
 370.3,
 377.5,
 200.5,
  41.5,
 132.5,
 209.5,
 220.3,
 193.3,
  64.1,
  15.4,
   4.5,
   5.1,
 135.9,
  14.5,
   8.7,
 144.5,
  28.9,
  11.1,
   9.3,
   1.8,
   0.0,
   3.3,
  15.8,
  31.7,
   4.1,
   5.9,
   3.5,
   1.8,
   1.9,
   7.7,
  17.7,
  51.9,
   0.5,
  31.3,
  82.2,
  14.5,
  99.8,
 223.5,
 182.0,
 222.0,
  71.4,
  55.3,
  89.6,
 187.9,
 233.9,
 399.1,
 405.1,
 193.7,
 308.0,
 237.8,
 404.5,
 981.4,
 662.2,
 380.9,
 314.5,
 452.3,
 613.1,
1205.4,
1256.6,
1536.6,
 949.5,
1000.8,
 380.4,
 802.1,
 739.9,
1047.1,
 768.0,
1282.1,
 709.5,
 706.5,
 840.5,
 825.5,
 460.2,
 996.7,
 442.5,
 635.4,
1116.3,
1117.1,
 635.6,
 668.8,
 605.2,
 ]

dr = pd.date_range('1874-05-31', periods=len(values), freq='M')

tsd = pd.Series(values, index=dr)

