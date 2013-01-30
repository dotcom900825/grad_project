/**
 * Based on Wookmark's endless scroll.
 */
var apiURL = '/api/activity/?format=json&offset='
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
          itemWidth: 600,
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
    var i=0, length=data.length, activity;
    for(; i<length; i++) {
      activity = data[i];
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
      html += "<div class='row' style='background-color:white; padding-top:20px; width:700px; margin-left:20%'>";
        html += "<div class='span3'>";
          html += '<img src=' + activity.userProfile.socialImageUrl +' />';
          html += '<ul>';
            html += '<li>';
              html += activity.userProfile.snsName;
            html += '</li>';
            html += '<li>';
              html += activity.userProfile.university;
            html += '</li>';
            html += '<li>';
              html += activity.userProfile.school;
            html += '</li>';
            html += '<li>';
              html += activity.userProfile.year_of_study;
            html += '</li>';
          html += '</ul>';
        html += '</div>';
        html += "<div class='span3'>";
          html += "<h3>";
            html += activity.title;
          html += "</h3>";
          html += "<div>";
            html += activity.description;
          html += "</div>";
           html += "<div>";
            html += activity.location;
          html += "</div>";
        html += "</div>"
      html += '</div>';
      html += '<hr />';
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
