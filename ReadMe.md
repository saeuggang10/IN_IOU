# IOU
-------------------------------
### 설명
```
 이미지 딥러닝 검증방법 중 하나로 실제 좌표와 예측좌표값을 교집합/합집합한 비율이 0.5이상일 때 제대로 검출되었다고 판단하는 알고리즘을 만들었다.
```

-------------------------------
-------------------------------

### package
```
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import os
import json
import glob
```

### input
```
target = '주소를 입력해주세요'
```

### code
1. 데이터 전처리
    * xlsx값에 데이터가 \n, 띄워쓰기, (, )이 있어 제대로 읽지 못함으로 숫자와 ,만 남도록 정리해준다

2. 좌표값
    * 좌표 값의 숫자 8개를 짝수, 홀수 리스트를 활용해 x, y값으로 나눠서 동적변수를 만든다
    * gpd.GeoSeries로 Polygon을 그린다
    
3. IOU
    * union : 합집합
    * intersection : 교집합
    * symdiff : 여집합
        * 3가지를 이용해 IOU값과 1-IOU값을 구해 df에 새 변수로 넣는다
    
4. df['difference']
    * 실제 IOU값과 알고리즘으로 만든 IOU_predict의 값을 비교해 알고리즘의 정밀도를 확인한다

-------------------------------
-------------------------------

#### 첨부파일
1. AngleCheck.zip
    * 코드 테스팅을 위한 파일
    
#### 주의사항
* plot의 geopandas패키지가 잘 실행되지 않을 수 있음으로 cmd에서 개별적인 설치가 필요함.

#### p.s.
* shaply, geopandas, matplotlib을 활용해 모두 계산해 보았으나 shaply와 geopandas가 거의 비슷했고, geopands가 좀 더 정확성이 높았다.