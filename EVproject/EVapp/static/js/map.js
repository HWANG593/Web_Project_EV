var positions = [];
var markers = [];
var locPosition;

$('#num0').click( function() {
  $.ajax({
      url:'http://localhost:8000/EVapp/loadMapData/0',
      dataType:'json',
      type:'GET',
      success:function(result){
          delmap();                                                
          mapdata(result);
          //console.log(positions);
      }
  });
});

$('#num1').click( function() {
    $.ajax({
        url:'http://localhost:8000/EVapp/loadMapData/1',
        dataType:'json',
        type:'GET',
        success:function(result){
            delmap();
            mapdata(result);
        }
    });
});

$('#num2').click( function() {
    $.ajax({
        url:'http://localhost:8000/EVapp/loadMapData/2',
        dataType:'json',
        type:'GET',
        //data:{'msg':$('#msg').val()},
        success:function(result){
            delmap();
            mapdata(result);
        }
    });
});

var mapContainer = document.getElementById('map'), // 지도를 표시할 div
mapOption = {
    center: new kakao.maps.LatLng(37.56682, 126.97865), // 지도의 중심좌표
    level: 6, // 지도의 확대 레벨
    mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
};

// 지도를 생성한다
var map = new kakao.maps.Map(mapContainer, mapOption);

// 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

// HTML5의 geolocation으로 사용할 수 있는지 확인합니다
if (navigator.geolocation) {
    // GeoLocation을 이용해서 접속 위치를 얻어옵니다
    navigator.geolocation.getCurrentPosition(function(position) {

        var lat = position.coords.latitude, // 위도
            lon = position.coords.longitude; // 경도

        locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
            message = '<div style="padding:5px;">현재 위치</div>'; // 인포윈도우에 표시될 내용입니다

        // 마커와 인포윈도우를 표시합니다
        displayMarker(locPosition, message);
      });

} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다

    var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
        message = 'geolocation을 사용할수 없어요..'
        displayMarker(locPosition, message);
}
console.log(locPosition);

// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function displayMarker(locPosition, message) {

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: locPosition
    });

    var iwContent = message, // 인포윈도우에 표시할 내용
        iwRemoveable = true;

    // 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({
        map: map,
        content : iwContent,
        removable : iwRemoveable
    });

    // 인포윈도우를 마커위에 표시합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map, marker);
    });

    // 지도 중심좌표를 접속위치로 변경합니다
    map.setCenter(locPosition);
}

//--------------------------------------------가져온 json 파일 올리는 부분-----------------------------------------------

function mapdata(attractions) {
  for (var i = 0; i < Object.keys(attractions).length; i++) {
    //주차료 여부에 따라 바꾸기
    if(attractions[i].fee == "Y" || attractions[i].fee == "y"){
      attractions[i].fee = "주차료 有"
    }
    if(attractions[i].fee == "N" || attractions[i].fee == "n"){
      attractions[i].fee = "주차료 없음"
    }

    //완속 충전 여부에 따라 바꾸기
    if(attractions[i].slowYN == "Y"){
      attractions[i].slowYN = "완속충전 가능 O"
    }
    if(attractions[i].slowYN == "N"){
      attractions[i].slowYN = " "
    }

    //급속 충전 여부에 따라 바꾸기
    if(attractions[i].fastYN == "Y"){
      attractions[i].fastYN = "급속충전 가능 O"
    }
    if(attractions[i].fastYN == "N"){
      attractions[i].fastYN = " "
    }
    
  var content = {
        title: attractions[i].title,
        latlng: new kakao.maps.LatLng(attractions[i].mapy, attractions[i].mapx),
        addr: attractions[i].addr,

        starttime: attractions[i].starttime,
        endtime: attractions[i].endtime,
        fee: attractions[i].fee,
        slowYN: attractions[i].slowYN,
        fastYN: attractions[i].fastYN,
        fasttype: attractions[i].fasttype,
        }
        positions.push(content);
    }
    drawMap();
};
  //console.log(positions);

function drawMap(){
// 마커 이미지의 이미지 주소입니다
  var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
  for (var i = 0; i < positions.length; i++) {
    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35);
    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
      map: map, // 마커를 표시할 지도
      position: positions[i].latlng, // 마커를 표시할 위치
      title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
      image: markerImage // 마커 이미지
    });
    markers.push(marker);

  (function(marker, place) {
    // 마크 클릭 시
    //console.log(typeof place.addr);

    kakao.maps.event.addListener(marker, 'click', function() {
      var overlay = new kakao.maps.CustomOverlay({

        // 오버레이에 띄울 내용
        content: '<div class="wrap">' +
              '    <div class="info">' +
              '        <div class="title">' +
                  place.title + '<div class="close" onclick="closeOverlay()" title="닫기"></div>' +
              '        </div>' +
              '        <div class="body">' +
              '                <div class="fee">' + place.fee + '</div>' +
              '            <div class="img">' +
              '                <img src= "../../static/img/kakaoMap.png" width="73" height="70">' +
              '           </div>' +
              '            <div class="desc">' +
              '                <div class="ellipsis">' + place.addr + '</div>' +
              '               <div class="jibun ellipsis"> 운영 시간 : ' + place.starttime +'<span> - </span>' + place.endtime + '</div>' +
              '                <div class="ellipsis"> >'+ place.slowYN +  place.fastYN + '</div>' +
              '                <div class="ellipsis">'+ place.fasttype + '</div>' +
              '            </div>' +
              '        </div>' +
              '    </div>' +
              '</div>',
        map: map,
        position: marker.getPosition()
      });

      // 커스텀 오버레이를 닫기 위해 호출되는 함수입니다
      function closeOverlay() {
          overlay.setMap(null);
      }

      // 아무데나 클릭하게되면 overlay를 끄기
      kakao.maps.event.addListener(map, 'click', function(mouseEvent) {
        overlay.setMap(null)
      })

      overlay.setMap(map);
    })
  })(marker, positions[i])
  }
}

function delmap(){
  for (var i = 0; i < markers.length; i++) {
        
    markers[i].setMap(null);  
    //positions[i]=null;    
  } 
  positions.length = 0;
  markers.length = 0;
}
function setCenter() {
    // 지도 중심을 이동 시킵니다
    map.setCenter(locPosition);

}