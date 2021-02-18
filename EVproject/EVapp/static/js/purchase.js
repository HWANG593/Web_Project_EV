$('#sub').click(function () {
    $.ajax({
        url: 'http://localhost:8000/EVapp/purchase/',
        //data: 'html',
        //type: 'GET',
        success: function (data) {
            var area = document.getElementById("sel1");
            var car = document.getElementById("sel2");
            var brand = document.getElementById("sel3");
            var area_money;
            var country_money;
            var sum;
            var country_money;

            // select element에서 선택된 option의 value가 저장된다.
            var sel1Value = area.options[area.selectedIndex].value;
            var sel2Value = car.options[car.selectedIndex].value;
            var sel3Value = brand.options[brand.selectedIndex].value;

            if(sel1Value ==''|| sel2Value == '' || sel3Value == ''){
                if (sel1Value == '')
                    alert("지역을 선택해주세요");
                else
                    alert("차종과 브랜드를 선택해주세요");
            }
            else{
                if (sel1Value == '서울') {
                    area_money = 400;
                }
                else if (sel1Value == '부산') {
                    area_money = 500;
                }
                else if (sel1Value == '대구') {
                    area_money = 450;
                }
                else if (sel1Value == '인천') {
                    area_money = 420;
                }
                else if (sel1Value == '광주') {
                    area_money = 500;
                }
                else if (sel1Value == '대전') {
                    area_money = 700;
                }
                else if (sel1Value == '울산') {
                    area_money = 550;
                }
                else if (sel1Value == '세종') {
                    area_money = 300;
                }
                else if (sel1Value == '경기') {
                    area_money = 500;
                }
                else if (sel1Value == '강원') {
                    area_money = 520;
                }
                else if (sel1Value == '충북') {
                    area_money = 800;
                }
                else if (sel1Value == '충남') {
                    area_money = 850;
                }
                else if (sel1Value == '전북') {
                    area_money = 900;
                }
                else if (sel1Value == '전남') {
                    area_money = 840;
                }
                else if (sel1Value == '경북') {
                    area_money = 850;
                }
                else if (sel1Value == '경남') {
                    area_money = 700;
                }
                else if (sel1Value == '제주') {
                    area_money = 400;
                }

                ////////////////////////////////////////////////////지역 끝

                if (sel3Value == '코나 (기본형)') {
                    country_money = 800;
                }
                else if (sel3Value == '코나 (경제형)') {
                    country_money = 690;
                }
                else if (sel3Value == '아이오닉 (HP)') {
                    country_money = 733;
                }
                else if (sel3Value == '아이오닉 (PTC)') {
                    country_money = 701;
                }
                else if (sel3Value == '니로 (HP)') {
                    country_money = 800;
                }
                else if (sel3Value == '니로 (PTC)') {
                    country_money = 780;
                }
                else if (sel3Value == '니로 EV') {
                    country_money = 717;
                }
                else if (sel3Value == '쏘울 (기본형)') {
                    country_money = 750;
                }
                else if (sel3Value == '쏘울 (도심형)') {
                    country_money = 688;
                }
                else if (sel3Value == 'ZOE ZEN') {
                    country_money = 722;
                }

                else if (sel3Value == 'ZOE INTENS ECO') {
                    country_money = 722;
                }
                else if (sel3Value == 'ZOE ITENS') {
                    country_money = 722;
                }
                else if (sel3Value == 'i3 120Ah Lux') {
                    country_money = 673;
                }

                else if (sel3Value == 'i3 120Ah SoL+') {
                    country_money = 673;
                }

                else if (sel3Value == '볼트 EV LT') {
                    country_money = 770;
                }

                else if (sel3Value == '볼트 EV Primier') {
                    country_money = 770;
                }

                else if (sel3Value == 'Peugeot e-208') {
                    country_money = 649;
                }

                else if (sel3Value == 'DS3 E-tense') {
                    country_money = 605;
                }

                else if (sel3Value == 'Peugeot e-2008') {
                    country_money = 605;
                }

                else if (sel3Value == 'Model S') {
                    country_money = 0;
                }

                else if (sel3Value == 'Model 3 (SRP RWD)') {
                    country_money = 684;
                }

                else if (sel3Value == 'Model 3 (Long Range)') {
                    country_money = 341;
                }

                else if (sel3Value == 'Model 3 (Performance)') {
                    country_money = 329;
                }

                else if (sel3Value == 'I-PACE EV400') {
                    country_money = 0;
                }

                else if (sel3Value == 'EQC 400 4M') {
                    country_money = 0;
                }

                else if (sel3Value == 'EQC 400 4MATIC') {
                    country_money = 0;
                }

                else if (sel3Value == 'e-tron 55 quattro') {
                    country_money = 0;
                }

                else if (sel3Value == 'SMART EV Z') {
                    country_money = 0;
                }

                //
                if (country_money >= 400){
                    price_coef = '100%';
                }
                if (country_money > 0){
                    price_coef = '50%';
                }
                if (country_money == 0){
                    price_coef = '0%';
                }

                country_money = (area_money/ 800)*country_money;
                sum = area_money + country_money;
                document.getElementById('area_money').innerText = area_money;
                document.getElementById('country_money').innerText = country_money;
                document.getElementById('sum').innerText = sum;
                document.getElementById('price_coef').innerText = price_coef;
            }
        }
    })
});


function categoryChange(e) {
   var car1 = [ "코나 (기본형)","코나 (경제형)","아이오닉 (HP)","아이오닉 (PTC)"];
   var car2 = ["니로 (HP)","니로 (PTC)","니로 EV","쏘울 (기본형)","쏘울 (도심형)"];
   var car3 = ["ZOE ZEN","ZOE INTENS ECO","ZOE ITENS"];
    var car4 = ["i3 120Ah Lux","i3 120Ah SoL+"];
    var car5 = ["볼트 EV LT","볼트 EV Primier"];
    var car6 = ["Peugeot e-208","DS3 E-tense","Peugeot e-2008"];
    var car7 = ["Model S","Model 3 (SRP RWD)","Model 3 (Long Range)","Model 3 (Performance)"];
    var car8 = ["I-PACE EV400"];
    var car9 = ["EQC 400 4M","  EQC 400 4MATIC"];
    var car10 = ["e-tron 55 quattro"];
    var car11 = ["SMART EV Z"];

   var target = document.getElementById("sel3");

   if(e.value == "현대") var d = car1;
   else if(e.value == "기아") var d = car2;
   else if(e.value == "르노삼성") var d = car3;
    else if(e.value == "BMW") var d = car4;
   else if(e.value == "GM") var d = car5;
    else if(e.value == "한불모터스") var d = car6;
   else if(e.value == "테슬라") var d = car7;
    else if(e.value == "재규어") var d = car8;
   else if(e.value == "벤츠 코리아") var d = car9;
    else if(e.value == "아우디") var d = car10;
   else if(e.value == "쎄미시스코") var d = car11;

   target.options.length = 0;

   for (x in d) {
      var opt = document.createElement("option");
      opt.value = d[x];
      opt.innerHTML = d[x];
      target.appendChild(opt);
   }
}