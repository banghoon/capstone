# -*- coding: utf-8 -*-
import torch
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration
import warnings
from pprint import pprint as pp


warnings.simplefilter('ignore')


def load_model(path='./kobart_summary'):
    model = BartForConditionalGeneration.from_pretrained(path)
    return model


def get_summary(texts: list, path='./kobart_summary'):
    model = load_model(path)
    tokenizer = get_kobart_tokenizer()
    outputs = []
    for text_ in texts:
        text_ = text_.replace('\n', '')[:2000]
        input_ids = tokenizer.encode(text_)
        input_ids = torch.tensor(input_ids)
        input_ids = input_ids.unsqueeze(0)
        output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
        outputs.append(tokenizer.decode(output[0], skip_special_tokens=True))
    return outputs


if __name__ == '__main__':

    text = ['''LG 트윈스 투수 임준형이 데뷔 첫 승을 거뒀다.

임준형은 26일 대전 한화생명이글스파크에서 열린 2021 신한은행 SOL KBO리그 한화 이글스전에 선발등판해 6이닝 3피안타 5탈삼진 2사사구 무실점을 기록했다. 팀의 4-0 승리로 임준형은 데뷔 첫 승을 달성했다.

임준형은 지난달 5일 kt전 5⅓이닝을 넘어 개인 한 경기 최다 이닝을 기록하는 동시에 선발 등판 4경기 만에 첫 퀄리티스타트까지 일구며 자신의 몫을 다했다. 5회까지 1점차 상황에서도 무실점 피칭을 이어갔다.

경기 후 류지현 LG 감독은 "임준형의 데뷔 첫 승을 축하하고 팀이 중요한 순간 정말 큰 힘이 됐다. 앞으로 더욱 기대가 된다"고 칭찬하기도 했다.

임준형은 "(팀 연패에 대한) 부담은 없었는데 전 경기에서 애매했다. 제구의 확실성이 떨어졌다. 전 경기가 좀 아쉬워서 그 생각을 가지고 하니까 긴장이 많이 됐다. 1회 더블아웃 나오고 나서 긴장이 풀렸다"고 등판 소감을 밝혔다.

포수로 호흡을 맞춘 베테랑 이성우는 그에게 계속 자신있게 던질 것을 주문했다. 임준형은 "주자 나갔을 때 너무 신경쓰지 말고 타자에 집중하라고 하셨다. 그리고 불안해하지 말라고 좋은 말씀 많이 해주셨다. 가운데로 던지라고 하셔서 슬라이더를 가운데로 던졌는데 좋은 결과가 나와서 감사하게 생각하고 있다"고 말했다.

임준형은 "초반에 기회를 먼저 받았는데 기대에 부응을 아예 못 해서 올해도 그냥 2군에서 하려다보다 했는데 김경태 코치님이라는 좋은 코치님을 만났다. 나를 아들 같이 대해주셨다. 너무 많은 도움이 됐다. 폼도 바꾸고 새롭게 시작했다. 김 코치님이 2군에서 좌절하고 있을 때도 항상 긍정적으로 말씀해주셨다"며 도움에 대한 감사 인사를 잊지 않았다.

임준형은 마지막으로 "1군 벤치에 앉아있는 것만으로도 기분 좋은데 기회 주시고 나가서 던지니까 꿈 같다. 남은 시즌은 더그아웃에서 파이팅을 열심히 외치겠다. 포스트시즌에서는 기회만 주면 다 던질 수 있을 것 같지만 벤치에서 파이팅만 해도 좋을 것 같다"고 남은 가을에 대한 각오를 전했다.
''', '''파이썬에서 selenium을 공부하던 중 크롬 드라이버를 실행시키면 터미널에 다음과 같은 에러가 발생했다. 정확한 에러메시지를 보게 되면

USB: usb_device_handle_win.cc:1049 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. 

와 같이 나타난다. 직역을 해보자면 USB에서 어떤걸 읽어오지 못했다는 것 같은데, USB를 사용하고 있지 않은데 위와 같은 에러메시지가 나오게 되니 당황했다.

사실 크롬 드라이버를 실행시키는 데 작동이 안되는 것과 같은 큰 오류는 아니지만 그래도 오류가 신경쓰이기에 해결 방법을 찾아나섰다. 
''']
    res = get_summary(text)
    pp(res)
