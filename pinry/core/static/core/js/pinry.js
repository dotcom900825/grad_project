/**
 * Based on Wookmark's endless scroll.
 */
var apiURL = '/api/pin/?format=json&offset='
var page = 0;
var handler = null;
var globalTag = null;
var isLoading = false;

/**
 * When scrolled all the way to the bottom, add more tiles.
 */
function onScroll(event) {
  if(!isLoading) {
      var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
      if(closeToBottom) loadData();
  }
};

function applyLayout() {
  $('#pins').imagesLoaded(function() {
      // Clear our previous layout handler.
      if(handler) handler.wookmarkClear();
      
      // Create a new layout handler.
      handler = $('#pins .pin');
      handler.wookmark({
          autoResize: true,
          offset: 10,
          itemWidth: 230,
          container: $('#pins')
      });
  });
};

/**
 * Loads data from the API.
 */
function loadData(tag) {
    isLoading = true;
    $('#loader').show();

    if (tag !== undefined) {
        globalTag = tag;
        window.history.pushState(tag, 'Pinry - Tag - '+tag, '/pins/tag/'+tag+'/');
    } else if (url(2) == 'tag') { //hard coded way to detect user input tag url
        tag = url(3);
        globalTag = tag;
        window.history.pushState(tag, 'Pinry - Tag - '+tag, '/pins/tag/'+tag+'/');
    }

    if (tag !== undefined) {
        $('#pins').html('');
        page = 0;
        if (tag != null)
            $('.tags').html('<span class="label tag" onclick="loadData(null)">' + tag + ' x</span>');
        else {
            $('.tags').html('');
            window.history.pushState(tag, 'Pinry - Recent Pins', '/pins/');
        }
    }

    var loadURL = apiURL+(page*30);
    if (globalTag !== null) loadURL += "&tag=" + tag;
    
    $.ajax({
        url: loadURL,
        success: onLoadData
    });
};

/**
 * Receives data from the API, creates HTML for images and updates the layout
 */
function onLoadData(data) {
    var user_pic = user_pic_url;
    var user_name = username;
    var submitter_name;
    var submitter_pic;

    data = data.objects;
    isLoading = false;
    $('#loader').hide();
    
    page++;
    
    var html = '';
    var i=0, length=data.length, image;
    for(; i<length; i++) {
      image = data[i];
     /* $.ajax({
            url: 'http://localhost:8000' + image.user + '?format=json',
            type: 'get',
            accepts: 'application/json',
            dataType: 'json',
            async: false,
            beforeSend: function(XMLHttpRequest){
              //ShowLoading();
            },
            success: function(data, textStatus){
               submitter_name = data.snsName;
               submitter_pic = data.socialImageUrl;
            },
            complete: function(XMLHttpRequest, textStatus){
              //HideLoading();
            },
            error: function(){
              //请求出错处理
            }
          });*/
      {
      html += '<div class="pin">';
          html += '<div class="pin-options">';
              html += '<a href="/pins/delete-pin/'+image.id+'">';
                  html += '<i class="icon-trash"></i>';
              html += '</a>';
          html += '</div>';
          html += "<h4 style='color:#F47D31; background-color:#fff; -webkit-box-shadow: 2px 2px 20px #888; -moz-box-shadow:2px 2px 20px #888; -webkit-transform:rotate(-45deg); -moz-transform:rotate(-45deg); position:absolute; text-align:center; left:-20px; margin-top:0px'>出售闲置</h4>";
       //   html += '<a class="fancybox" rel="pins" href="'+image.image+'">';
              html += "<a  rel='pins' href='/item/" + image.id + "/detail/'>";
              html += '<img src="'+image.thumbnail+'" width="200" >';
          html += '</a>';
          html += "<div style='border-bottom:1px solid #ddd'>";
          if (image.description) html += "<p style='padding-bottom:5px; border: 1px solid #DDDDD'>"+ image.description+'</p>';
          html += '</div>';
          if (image.price) html +="<p style='padding-top:5px; border-bottom: 1px solid #DDD'>价格: " + image.price + '元</p>';
          if (image.tags) {
              html += "<div class='clearfix' style='margin-bottom:5px'>";
              html += '<p>';
              html += "<a style='width:30px;height:30px' href='/accounts/" + image.userProfile.snsName + "'> <img style='width:30px; height:30px' src='" + image.userProfile.socialImageUrl + "' /></a>";
              html += "<span> " + image.userProfile.snsName + " 发布在</span>"
              for (tag in image.tags) {
                  html += '<span class="label tag" onclick="loadData(\'' + image.tags[tag] + '\')">' + image.tags[tag] + '</span> ';
              }
              html += '</p>';
              html += '</div>';
          }
          if(user_auth_flag == "True")
          {
            html += "<div class='write convo clearfix' style='display:block'><a href='/accounts/" + user_name + "' title='' class='img x'><img style='width:30px; height:30px'  src='" + user_pic + "'/></a><form action='/messages/compose/" + image.userProfile.user.username + "/' method='POST'> <input type='hidden' name='item' value='" + image.id + "'/> <input type='hidden' name='to' value='" + image.userProfile.user.username + "'/> <textarea name='body' style='background-color: rgb(255, 255, 255);' autocomplete='off' placeholder='感兴趣吗？留个言吧！' class='GridComment ani-affected '></textarea><input type='submit' value='留言' name='send' class='btn btn-info grid_comment_button'/></form></div>";
          }
          else
          {
            html += "<div class='write convo clearfix' style='display:block'><a class='img x'><img src='/static/vendor/utility/user2.jpg' style='width:30px; height:30px'/></a><form action='/messages/compose/" + image.userProfile.user.username + "/' method='POST'> <input type='hidden' name='to' value='" + image.userProfile.user.username + "'/> <textarea name='body' style='width:160px; padding-right:0px; background-color: rgb(255, 255, 255);' autocomplete='off' placeholder='还没有登录，没法留言哦亲!' class='GridComment ani-affected '></textarea></form></div>";
          }
      html += '</div>';
      }
    }
    
    $('#pins').append(html);
    
    applyLayout();
};

$(document).ready(new function() {
    $(document).bind('scroll', onScroll);
    loadData();
    $("#example").popover(); 
});


/**
 * On clicking an image show fancybox original.
 */
/*$('.fancybox').fancybox({
    openEffect: 'none',
    closeEffect: 'none'
});*/
