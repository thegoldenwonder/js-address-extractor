#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NB: coding above is important since the interpreter assumes ASCII without it (when there is #! as well)
# The HTML below can't be parsed as ASCII, so this is necessary.

import zerorpc
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

html = """


<!doctype html>
<html lang="en" dir="ltr" class="no-js"> 
<head>
  <meta http-equiv="X-UA-Compatible" content="IE=9; IE=8; IE=7; IE=EDGE,chrome=1" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0 maximum-scale=2.0 user-scalable=yes" />
  <!--[if IE]><![endif]-->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="http://www.ox.ac.uk/sites/default/themes/custom/oxweb/favicon.ico" />
<meta name="Generator" content="Mothership (http://mothershipthe.me)" />
<link rel="apple-touch-icon-precomposed" href="http://www.ox.ac.uk/sites/default/themes/custom/oxweb/apple-touch-icon-114x114.png" />
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=867549083324614&amp;ev=PageView&amp;noscript=1" />
</noscript>
<link rel="apple-touch-icon" href="http://www.ox.ac.uk/sites/default/themes/custom/oxweb/apple-touch-icon-114x114.png" />
<link rel="canonical" href="http://www.ox.ac.uk/contact-us" />
<link rel="shortlink" href="http://www.ox.ac.uk/node/1798" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:creator" content="@UniofOxford" />
<meta name="twitter:creator:id" content="48289662" />
<meta name="twitter:title" content="Contact us | University of Oxford" />
  <link rel="apple-touch-icon" sizes="144x144" href="http://www.ox.ac.uk/sites/default/themes/custom/oxweb/apple-touch-icon-144x144.png"/><link rel="apple-touch-icon" sizes="114x114" href="http://www.ox.ac.uk/sites/default/themes/custom/oxweb/apple-touch-icon-114x114.png"/>
<link rel="apple-touch-icon" sizes="72x72" href="http://www.ox.ac.uk/sites/default/themes/custom/oxweb/apple-touch-icon-72x72.png"/>
<link rel="apple-touch-icon" href="http://www.ox.ac.uk/sites/default/themes/custom/oxweb/apple-touch-icon.png"/>
  <title>Contact us | University of Oxford</title>
  <link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__BJ6Ou6QsBRtnFTmxaakamOIS8n4QswDP2XnnZ1sxtaM__NBuvkP6eInGIkb1aJvUHx5PX79XApuxBDkk_77W5tYk__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__8RxQy0xV_wXwSOYutnN8oWnucXmxC_xDlWDoZoaE6ig__vMWO9DZNya8H_HBxRsCzkHo5dKR4oumpePjqMHgaSN0__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__STxzdsGaJQwmsXOyFqd7Mi31ZIo3KJ2aA4k7t5MP4dM__JtfQ_kdVQJ1bfz9IY0NpSu0ede5WGJ-1XoV12GIpPo8__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
<link rel="stylesheet" href="//fonts.googleapis.com/css?family=PT+Sans:400,700,400italic,700italic|PT+Sans+Narrow:400,700|PT+Serif:400,700,400italic&amp;subset=latin,latin-ext" />
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__XGG8-Ss0119yRrV6Wouz-NYqsNf0pp5HuEC_i2_SqVs__tcbvxPSb9ssLFeky6SSVtabN2FbE7f6agfrZBZU6vlI__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__ByI_Pi9EU2-37BimrxBkQItJJ40AVOd8Gvq7GnTw17M__KUi7MDUlCxmG2ffdiIwVmAoLyMZnIgdmqLekuG9FU44__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" media="print" />

<!--[if IE]>
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__OnsWsoadeugiGFqDk5vbKlGgN4L9Oekc91phquZqEZI__r8xUxB5d-MbSJE2P__l9mZbfmtYY-XoRNe1nPrEcs4U__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
<![endif]-->

<!--[if IE 8]>
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__Dbom7S8ZtGw1HDgq4XX5Gm9UdDKuz2XfeyOn1reAzXk__imxrN75RBhwxS-PAq41Niv17L0iMRxqmcJKhLTop9vQ__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
<![endif]-->
<style>.shared-event-styling .content-meta{margin-top:2.4em;}.shared-event-styling .node-event-past{opacity:0.5;filter:alpha(opacity=50);}.shared-event-styling .view-mode-oxweb_full_content .field-label-inline,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single{*zoom:1;}.shared-event-styling .view-mode-oxweb_full_content .field-label-inline:before,.shared-event-styling .view-mode-oxweb_full_content .field-label-inline:after,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single:before,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single:after{display:table;content:"";line-height:0;}.shared-event-styling .view-mode-oxweb_full_content .field-label-inline:after,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single:after{clear:both;}.shared-event-styling .view-mode-oxweb_full_content .field-label-inline label,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single label{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline;float:left;width:33.333333333333%;padding:0 0;*width:30.208333333333%;*padding:0 -0.03125px;min-width:27%;}@media only screen and (max-width:870px){.shared-event-styling .view-mode-oxweb_full_content .field-label-inline label,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single label{width:100%;float:none;display:block;}}.shared-event-styling .view-mode-oxweb_full_content .field-label-inline .field-item-single,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single .field-item-single{float:left;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline;width:66.666666666667%;padding:0 0;*width:63.541666666667%;*padding:0 -0.03125px;}@media only screen and (max-width:870px){.shared-event-styling .view-mode-oxweb_full_content .field-label-inline .field-item-single,.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single .field-item-single{width:100%;float:none;display:block;}}.shared-event-styling .view-mode-oxweb_full_content .field-name-field-event-venue-details span.field-item-single{float:none;margin-left:33.3%;display:block;}.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single .field-item-single{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline;float:left;width:66.666666666667%;padding:0 0;*width:63.541666666667%;*padding:0 -0.03125px;}@media only screen and (max-width:870px){.shared-event-styling .view-mode-oxweb_full_content .field-name-event-speakers-custom .field-item-single .field-item-single{width:100%;float:none;display:block;}}.shared-event-styling .view-mode-oxweb_full_content .field-type-date{font-family:"PT Serif",Georgia,'Times New Roman',serif;}.shared-event-styling .view-mode-oxweb_full_content .group_event_meta{border-top:1px solid #e0ded9;border-bottom:1px solid #e0ded9;font-size:1.125em;line-height:1.5em;margin:0 18% 2em 0;padding:2em 0;}.shared-event-styling .view-mode-oxweb_full_content .group_event_meta .field-name-field-event-venue-details p:only-child{margin-bottom:0;}.shared-event-styling .view-mode-oxweb_full_content .leaflet-container{margin-bottom:2.5em;max-width:90%;}.page-header{position:relative;}.page-header .row{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline;float:left;width:100%;padding:0 2.118933698%;*width:96.875%;*padding:0 2.087683698%;min-height:160px;}@media only screen and (max-width:870px){.page-header .row{width:100%;float:none;display:block;}}.page-header .site-header-top{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;margin-left:111px;padding-right:167px;padding-left:2.118933698%;min-height:49px;}.page-header .site-header-bottom{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;margin-left:0;display:block;margin-left:111px;padding-left:2.118933698%;position:relative;min-height:41px;margin-top:1em;}.oxweb-primary-menu-block{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline;float:left;width:58.333333333333%;padding:0 0;*width:55.208333333333%;*padding:0 -0.03125px;display:block;}@media only screen and (max-width:870px){.oxweb-primary-menu-block{width:100%;float:none;display:block;}}.oxweb-secondary-menu-block{width:100%;}#toolbar{z-index:99999;}header.page-header{text-align:center;width:100%;margin:0 auto;z-index:9999;}header.page-header .row{background:#002147;font-family:"PT Sans",'Helvetica Neue',Arial,Helvetica,sans-serif;float:none;display:block;padding-top:1.5625em;padding-bottom:1em;-webkit-transition:padding 0.35s;-moz-transition:padding 0.35s;-o-transition:padding 0.35s;transition:padding 0.35s;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}.logo{float:left;width:111px;margin-right:-100%;position:relative;z-index:2;}.logo a.square{width:110px;height:110px;display:block;background:url('/sites/default/themes/custom/oxweb/images/oxweb-logo.gif') no-repeat center center;overflow:hidden;text-indent:-9999%;}@media (-webkit-min-device-pixel-ratio:2),(min-resolution:192dpi){.logo a.square{background:url('/sites/default/themes/custom/oxweb/images/oxweb-logo-square.svg') no-repeat center center;background-size:100% 100%;image-rendering:-moz-crisp-edges;image-rendering:-o-crisp-edges;image-rendering:-webkit-optimize-contrast;image-rendering:optimize-contrast;-ms-interpolation-mode:bicubic;image-rendering:optimizeQuality;}}.menu-wrapper{width:100%;float:left;}.site-header-bottom .oxweb-secondary-menu-block ul li.expanded ul li a{background:transparent;}.oxweb-primary-menu-block,.oxweb-secondary-menu-block{text-align:left;text-transform:uppercase;font-family:"PT Sans",'Helvetica Neue',Arial,Helvetica,sans-serif;color:#fff;}.oxweb-primary-menu-block a,.oxweb-secondary-menu-block a{opacity:0.7;filter:alpha(opacity=70);color:#fff;}.oxweb-primary-menu-block a.active,.oxweb-primary-menu-block a:active,.oxweb-primary-menu-block a:visited,.oxweb-primary-menu-block a:hover,.oxweb-primary-menu-block a.active-trail,.oxweb-secondary-menu-block a.active,.oxweb-secondary-menu-block a:active,.oxweb-secondary-menu-block a:visited,.oxweb-secondary-menu-block a:hover,.oxweb-secondary-menu-block a.active-trail{opacity:1;filter:alpha(opacity=100);color:#fff;text-decoration:none;}.oxweb-primary-menu-block ul,.oxweb-secondary-menu-block ul{float:left;padding:0;margin:0;}.oxweb-primary-menu-block ul li,.oxweb-primary-menu-block ul li.expanded,.oxweb-secondary-menu-block ul li,.oxweb-secondary-menu-block ul li.expanded{display:inline-block;padding:0;list-style-image:none;list-style-type:none;}.oxweb-primary-menu-block ul li a,.oxweb-primary-menu-block ul li.expanded a,.oxweb-secondary-menu-block ul li a,.oxweb-secondary-menu-block ul li.expanded a{padding:10px 25px 15px 10px;}.oxweb-primary-menu-block ul li.expanded,.oxweb-secondary-menu-block ul li.expanded{position:relative;}.oxweb-primary-menu-block ul li.expanded a,.oxweb-secondary-menu-block ul li.expanded a{background:url('/sites/default/themes/custom/oxweb/images/menu_arrow.png') 94% 1.2em no-repeat;background-position:right 10px top 1.3em;padding-right:25px;}.oxweb-primary-menu-block ul li.expanded ul a,.oxweb-secondary-menu-block ul li.expanded ul a{background-image:none;padding-right:0;}.oxweb-primary-menu-block{font-size:0.78em;}.oxweb-secondary-menu-block{display:table-row;}.oxweb-secondary-menu-block h2.title,.oxweb-secondary-menu-block ul li,.oxweb-secondary-menu-block ul li.expanded{display:table-cell;vertical-align:top;padding:0;border-right:1px solid rgba(255,255,255,0.07);-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}.oxweb-secondary-menu-block h2.title ul li,.oxweb-secondary-menu-block ul li ul li,.oxweb-secondary-menu-block ul li.expanded ul li{float:none;max-width:none;min-width:215px;}.oxweb-secondary-menu-block ul li,.oxweb-secondary-menu-block ul li.expanded{line-height:1.05em;max-width:200px;}.oxweb-secondary-menu-block ul li a,.oxweb-secondary-menu-block ul li.expanded a{padding:10px;padding-top:8px;line-height:1.2em;display:inline-block;}.oxweb-secondary-menu-block ul li.expanded a{padding-right:30px;}.oxweb-secondary-menu-block ul li.expanded ul a{height:auto;}.oxweb-secondary-menu-block h2.title{font-size:1.5em;line-height:1.05em;font-weight:normal;margin:0;padding:8px 36px 20px 7px;background:url('/sites/default/themes/custom/oxweb/images/menu-chevron.png') no-repeat 97.5% top;border-right:0;vertical-align:top;}.site-header-top ul li.expanded a{position:relative;z-index:7;background-position:right 9px top 1.6em;}.site-header-top ul li.expanded:hover a{background-position:right 9px top -1.95em;}.site-header-bottom ul li.expanded a{position:relative;background-position:right 15px top 0.90em;}.site-header-bottom ul li.expanded:hover a{background-position:right 15px top -101px;z-index:5;}.oxweb-secondary-menu-block-noh2 ul ul{margin-left:0;}body.sticky-header-collapsed .logo{display:none;}body.sticky-header-collapsed .page-header{position:fixed;}body.sticky-header-collapsed .page-header .row{padding-top:0.75em;padding-bottom:0.75em;-webkit-transition:padding 0.35s;-moz-transition:padding 0.35s;-o-transition:padding 0.35s;transition:padding 0.35s;min-height:72px;padding-right:0;}body.sticky-header-collapsed #block-google-appliance-ga-block-search-form{top:-6px;width:200px;height:62px;}body.sticky-header-collapsed #block-google-appliance-ga-block-search-form .form-item input[type=text]{-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;width:200px;height:62px;background-color:#fff;}body.sticky-header-collapsed #block-google-appliance-ga-block-search-form.toggle{background-color:rgba(255,255,255,0.1);width:66px;height:62px;min-width:0;}body.sticky-header-collapsed #block-google-appliance-ga-block-search-form.toggle .form-item input[type=text]{display:none;}body.sticky-header-collapsed .block-google-appliance input[type=submit]{top:15px;right:21px;}body.sticky-header-collapsed .site-header-top{display:none;}body.sticky-header-collapsed .site-header-bottom{width:100%;float:left;margin-top:0;margin-left:0;padding-left:0;}body.sticky-header-collapsed .site-header-bottom .oxweb-secondary-menu-block ul{margin-right:65px;}body.sticky-header-collapsed .site-header-bottom .oxweb-secondary-menu-block ul li,body.sticky-header-collapsed .site-header-bottom .oxweb-secondary-menu-block ul li.expanded{vertical-align:top;}body.sticky-header-collapsed .site-header-bottom .oxweb-secondary-menu-block ul li.last ul{right:-65px;}body.sticky-header-collapsed .page-header-row .oxweb-secondary-menu-block.homepage-oxweb-secondary-menu{position:absolute;bottom:4px;width:58%;}body.sticky-header-collapsed .page-header-row .homepage-role-base-menu{margin-right:85px;}.page-header-row .oxweb-secondary-menu-block.homepage-oxweb-secondary-menu{position:absolute;bottom:35px;width:56%;}.page-header-row .oxweb-secondary-menu-block.homepage-oxweb-secondary-menu ul li.expanded:hover a{background-position:right 15px top -1.3em;}.page-header-row .oxweb-secondary-menu-block.homepage-oxweb-secondary-menu ul li.expanded:hover a:hover{background-position:right 15px top 0.90em;}.page-header-row .oxweb-secondary-menu-block.homepage-oxweb-secondary-menu ul li a{opacity:1;filter:alpha(opacity=100);font-size:1.313em;white-space:nowrap;}.page-header-row .homepage-role-base-menu{font-size:0.813em;text-transform:none;float:right;width:52.5%;}.page-header-row .homepage-role-base-menu ul{float:right;}.page-header-row .homepage-role-base-menu ul li a{font-size:1.125em;padding-left:0;padding-right:0;margin-right:1.5em;}.page-header-row .homepage-role-base-menu ul li.last a{margin-right:0.4375em;}.page-header-row .homepage-role-base-menu ul li.expanded a{background:none;}h1,h2,h3,h4,h5,h6{font-family:"PT Sans",'Helvetica Neue',Arial,Helvetica,sans-serif;margin:0 0 0.5em 0;line-height:1.2em;color:#333333;}h1{font-size:3.125em;font-weight:700;font-family:"PT Sans",'Helvetica Neue',Arial,Helvetica,sans-serif;margin:0 0 0.5em 0;line-height:1.05em;}.main-content h1{margin-right:18%;}body.page-full-width .main-content h1{margin-right:2.118933698%;}h2{font-size:1.625em;font-weight:700;}h3{font-size:1.313em;font-weight:400;}h4{font-size:16px;}h5{font-size:16px;}h6{font-size:16px;}.main-content h2,.main-content h3,.main-content h4,.main-content h5,.main-content h6{margin:1.6em 0 0.5em 0;}.block-menu h2,.block-nice-menus h2{margin:0;padding:0;height:1px;height:0px;overflow:hidden;text-indent:-9999%;}
</style>
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__V5lUSZEHBBuABP-buuYT9zHkVLe2MvQBhGwN1kA0Dno__FJKm6JrHf6lmR1T6CVZwwXZA7iaEhr9vXRHYVM0Rb7M__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
<link rel="stylesheet" href="//www.ox.ac.uk/sites/files/oxford/advagg_css/css__zolETMGHO1YJUVTFIn7nL0G8b__M3qc0x2hAPc3xDd0__Mb2CTBeWOwfHgatgFskUJJQN0bnr1BrOSYrkZjBTF6I__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.css" />
  <script src="//www.ox.ac.uk/sites/files/oxford/advagg_js/js__q4ZluDEr7yHOp8TDo4l-cypOrRNOvxyaxrSrBudwQ2E__ktfy3vRZCP1kqHMr0STpLbgL2jP61kiGIl64IhbE_Sk__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.js"></script>
<script src="//www.ox.ac.uk/sites/files/oxford/advagg_js/js__T73ujsOjK-1cyTby7fEe8eK8r1o3_6UM-pyXbhgxLPM__ZQUill7DCw6Tj20_aEunc3YLkP00ibvBCy6XvZLzRLg__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.js"></script>
<script src="//www.ox.ac.uk/sites/files/oxford/advagg_js/js__fpAVZm8nCIsFzZw6riH8so3-I5cAZkb0Emsb0yqD660__cjdgqsvK6scyPJAi667oxGAet4H_p4Ahl_B-vdUne9A__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-ajaxtransport-xdomainrequest/1.0.2/jquery.xdomainrequest.min.js"></script>
<script src="//cdn.rawgit.com/ox-it/contacts-widget/6f2d0b7de893ab1973f86382632189b93bfefd91/widget/contact_search.js"></script>
<script src="//www.ox.ac.uk/sites/files/oxford/advagg_js/js__iZhtjLs0os5QX1Q_hd8NBwEVQJeWHlGcMN2KVU4RFHo__MU3G7eA2mgMWeDhhVF-wSy41Mteu05nNEQ7jpzAj3cM__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.js"></script>
<script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "UA-53948675-1", {"cookieDomain":".ox.ac.uk"});ga('require', 'displayfeatures');ga("send", "pageview");ga('create', 'UA-44722553-1', 'ox.ac.uk', {'name': 'oxRollUpTracker'} );
ga('oxRollUpTracker.require', 'displayfeatures');
ga('oxRollUpTracker.send', 'pageview');</script>
<script src="//www.ox.ac.uk/sites/files/oxford/advagg_js/js__5AkQ32eKyH4bHoZwRq2mAxZB8_fSkxwahmo58o-EFPg__zYEQ1RTErz3p0HqBAZn45I2wbYNbT9CcklAQVZxOqV0__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.js"></script>
<script><!-- Facebook Pixel Code -->
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,"script","//connect.facebook.net/en_US/fbevents.js");

fbq("init", "867549083324614");
fbq("track", "PageView");
  <!-- End Facebook Pixel Code --></script>
<script src="//www.ox.ac.uk/sites/files/oxford/advagg_js/js__sTOYibCHX3PjvTSi945x_NFLxlyRyMdT-ekCCJgHakQ__0IQ7PuegtqdPbOiUAAZudY4McK0fKI3ESOLn0V6xe9M__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.js"></script>
<script src="//www.ox.ac.uk/sites/files/oxford/advagg_js/js__NApEfNetOv0iKOaiS8Z3hqHIRkgSK5NwyYcTjOiwNcs__nU_o07hwDYQElVgKUXzcqwfuvwue_VigA-SzFLZXySU__uQdxwZbyDYU_kCDyd_6-dJxq7TKBrVKDxAQ7-fFl_N8.js"></script>
<script>jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"oxweb","theme_token":"lH9ONjgy9ILpcSuauaCU_Z0OEnubkgtb0l0r-peqdP4","jquery_version":"1.10","css":{"modules\/system\/system.base.css":1,"modules\/system\/system.menus.css":1,"modules\/system\/system.messages.css":1,"modules\/system\/system.theme.css":1,"sites\/all\/modules\/colorbox_node\/colorbox_node.css":1,"modules\/comment\/comment.css":1,"sites\/all\/modules\/date\/date_api\/date.css":1,"sites\/all\/modules\/date\/date_popup\/themes\/datepicker.1.7.css":1,"sites\/all\/modules\/domain\/domain_nav\/domain_nav.css":1,"modules\/field\/theme\/field.css":1,"sites\/all\/modules\/google_appliance\/theme\/google_appliance.css":1,"sites\/all\/modules\/logintoboggan\/logintoboggan.css":1,"sites\/all\/modules\/mollom\/mollom.css":1,"modules\/node\/node.css":1,"modules\/user\/user.css":1,"sites\/all\/modules\/views\/css\/views.css":1,"sites\/all\/modules\/colorbox\/styles\/plain\/colorbox_style.css":1,"sites\/all\/modules\/cookienotice\/cookienotice.css":1,"sites\/all\/modules\/ctools\/css\/ctools.css":1,"sites\/all\/modules\/shib_auth\/shib_auth.css":1,"sites\/all\/modules\/field_group\/field_group.css":1,"https:\/\/fonts.googleapis.com\/css?family=PT+Sans:400,700,400italic,700italic|PT+Sans+Narrow:400,700|PT+Serif:400,700,400italic\u0026subset=latin,latin-ext":1,"sites\/all\/themes\/mothership\/mothership\/css\/reset.css":1,"sites\/all\/themes\/mothership\/mothership\/css\/reset-html5.css":1,"sites\/all\/themes\/mothership\/mothership\/css\/mothership-default.css":1,"sites\/all\/themes\/mothership\/mothership\/css\/mothership.css":1,"sites\/default\/themes\/custom\/oxweb\/css\/yui\/reset-min.css":1,"sites\/default\/themes\/custom\/oxweb\/css\/yui\/base-min.css":1,"sites\/default\/themes\/custom\/oxweb\/css\/yui\/fonts-min.css":1,"sites\/default\/themes\/custom\/oxweb\/css\/site.less":1,"sites\/default\/themes\/custom\/oxweb\/css\/search.less":1,"sites\/default\/themes\/custom\/oxweb\/css\/menu.less":1,"sites\/default\/themes\/custom\/oxweb\/css\/maintenance.css":1,"sites\/default\/themes\/custom\/oxweb\/field_collection.theme.css":1,"sites\/default\/themes\/custom\/oxweb\/css\/alternative\/print.less":1,"sites\/default\/themes\/custom\/oxweb\/css\/ie\/ie.less":1,"sites\/default\/themes\/custom\/oxweb\/css\/ie\/ie8.less":1,"0":1,"sites\/default\/themes\/custom\/oxweb\/css\/types\/page.less":1,"sites\/default\/themes\/custom\/oxweb\/css\/alternative\/mobile.less":1},"js":{"sites\/all\/modules\/jquery_update\/replace\/jquery\/1.10\/jquery.min.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"misc\/ajax.js":1,"sites\/all\/modules\/jquery_update\/js\/jquery_update.js":1,"sites\/all\/libraries\/colorbox\/jquery.colorbox-min.js":1,"sites\/all\/modules\/colorbox\/js\/colorbox.js":1,"sites\/all\/modules\/colorbox\/styles\/plain\/colorbox_style.js":1,"sites\/all\/modules\/colorbox\/js\/colorbox_load.js":1,"sites\/all\/modules\/cookienotice\/cookienotice.js":1,"sites\/all\/modules\/media_colorbox\/media_colorbox.js":1,"\/\/cdnjs.cloudflare.com\/ajax\/libs\/jquery-ajaxtransport-xdomainrequest\/1.0.2\/jquery.xdomainrequest.min.js":1,"\/\/cdn.rawgit.com\/ox-it\/contacts-widget\/6f2d0b7de893ab1973f86382632189b93bfefd91\/widget\/contact_search.js":1,"sites\/default\/modules\/custom\/oxweb_contact_search\/oxweb_contact_search.js":1,"sites\/all\/modules\/google_analytics\/googleanalytics.js":1,"sites\/all\/modules\/field_group\/field_group.js":1,"misc\/progress.js":1,"sites\/all\/modules\/colorbox_node\/colorbox_node.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/vendor\/carouFredSel-6.2.1.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/vendor\/jquery.touchSwipe.min.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/vendor\/jquery-migrate-1.2.1.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/site.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/vendor\/html5.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/vendor\/harvey.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/media-queries.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/vendor\/jquery.fitvids.js":1,"sites\/default\/themes\/custom\/oxweb\/js\/vendor\/stupidtable.min.js":1}},"colorbox":{"transition":"elastic","speed":"350","opacity":"0.85","slideshow":false,"slideshowAuto":true,"slideshowSpeed":"2500","slideshowStart":"start slideshow","slideshowStop":"stop slideshow","current":"{current} of {total}","previous":"\u00ab Prev","next":"Next \u00bb","close":"Close","overlayClose":true,"maxWidth":"100%","maxHeight":"100%","initialWidth":"300","initialHeight":"250","fixed":true,"scrolling":true,"mobiledetect":true,"mobiledevicewidth":"500px"},"cookieNotice":{"alertText":"We use cookies to help give you the best experience on our website. By continuing without changing your cookie settings, we assume you agree to this. Please read our \u003Ca href=\u0022\/cookies-privacy-policy\u0022\u003Ecookie policy\u003C\/a\u003E to find out more.","closeText":"Dismiss","domainroot":".ox.ac.uk"},"googleanalytics":{"trackOutbound":1,"trackMailto":1,"trackDownload":1,"trackDownloadExtensions":"7z|aac|arc|arj|asf|asx|avi|bin|csv|doc(x|m)?|dot(x|m)?|exe|flv|gif|gz|gzip|hqx|jar|jpe?g|js|mp(2|3|4|e?g)|mov(ie)?|msi|msp|pdf|phps|png|ppt(x|m)?|pot(x|m)?|pps(x|m)?|ppam|sld(x|m)?|thmx|qtm?|ra(m|r)?|sea|sit|tar|tgz|torrent|txt|wav|wma|wmv|wpd|xls(x|m|b)?|xlt(x|m)|xlam|xml|z|zip","trackDomainMode":"1","trackCrossDomains":["http:\/\/ox-staging-oxfordtoday.torchboxapps.com","http:\/\/ox-staging.torchboxapps.com","http:\/\/www.oxfordtoday.ox.ac.uk","http:\/\/www.ox.ac.uk"]},"urlIsAjaxTrusted":{"\/contact-us":true}});</script>
  </head>

<body class="not-front not-logged-in one-sidebar sidebar-second page-node page-node- page-node-1798 node-type-page domain-oxweb no-sidebar-first page-contact-us" >
<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-TDB29T" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script type="text/javascript">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0];var j=d.createElement(s);var dl=l!='dataLayer'?'&l='+l:'';j.src='//www.googletagmanager.com/gtm.js?id='+i+dl;j.type='text/javascript';j.async=true;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-TDB29T');</script>
<!-- End Google Tag Manager -->
  <div id="skip-link">
    <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
  </div>
    
      
  <section id="visible-body">
      <header class="page-level page-header">
    <div class="wrapper">
      <div id="page-header-row" class="row page-header-row">
        <div class="logo">
          <a class="square" href="/" title="Home" id="site-name-square">Home</a>
          <a class="rect" href="/" title="Home" id="site-name-rec">Home</a>
        </div>
        <div class="menu-wrapper">
          <div id="site-header-top" class="site-header-top">
                                  </div>
                    <div id="site-header-bottom" class="site-header-bottom">
                       
    
<nav  id="block-menu-block-4" class="block block-menu-block oxweb-secondary-menu-block oxweb-secondary-menu-block-noh2 homepage-oxweb-secondary-menu block-menu-block-4 " role="navigation">
  
      
  <ul><li class="first expanded menu-mlid-2711"><a href="/admissions">Admissions</a><ul><li class="first leaf has-children menu-mlid-2511"><a href="/admissions/undergraduate">Undergraduate</a></li>
<li class="leaf has-children menu-mlid-2878"><a href="/admissions/graduate">Graduate</a></li>
<li class="last leaf has-children menu-mlid-1215"><a href="/admissions/continuing-education">Continuing education</a></li>
</ul></li>
<li class="expanded menu-mlid-2549"><a href="/research">Research</a><ul><li class="first leaf menu-mlid-2019"><a href="/about/organisation/strategic-plan/research" title="">Research strategy</a></li>
<li class="leaf menu-mlid-2020"><a href="/research/divisions">Divisions</a></li>
<li class="leaf has-children menu-mlid-5389"><a href="/research/research-impact">Research impact</a></li>
<li class="leaf menu-mlid-2727"><a href="/research/libraries">Libraries</a></li>
<li class="leaf has-children menu-mlid-5123"><a href="/research/innovation-and-partnership">Innovation and Partnership</a></li>
<li class="leaf has-children menu-mlid-3934"><a href="/research/support-researchers">Support for researchers</a></li>
<li class="last leaf has-children menu-mlid-5324"><a href="/research/research-in-conversation">Research in conversation</a></li>
</ul></li>
<li class="expanded menu-mlid-1105"><a href="/news-and-events" title="">News &amp; Events</a><ul><li class="first leaf has-children menu-mlid-2137"><a href="/events-list">Events</a></li>
<li class="leaf menu-mlid-2435"><a href="/news/science-blog">Science Blog</a></li>
<li class="leaf menu-mlid-2438"><a href="/news/arts-blog">Arts Blog</a></li>
<li class="leaf menu-mlid-3014"><a href="/news-and-events/for-journalists" title="">News releases for journalists</a></li>
<li class="leaf menu-mlid-2680"><a href="/news-and-events/filming-in-oxford">Filming in Oxford</a></li>
<li class="last leaf menu-mlid-5738"><a href="/news-and-events/find-an-expert">Find An Expert</a></li>
</ul></li>
<li class="last expanded menu-mlid-1892"><a href="/about">About</a><ul><li class="first leaf has-children menu-mlid-1326"><a href="/about/organisation">Organisation</a></li>
<li class="leaf has-children menu-mlid-1350"><a href="/about/facts-and-figures">Facts and figures</a></li>
<li class="leaf has-children menu-mlid-2800"><a href="/about/oxford-people">Oxford people</a></li>
<li class="leaf has-children menu-mlid-1381"><a href="/about/increasing-access">Increasing access</a></li>
<li class="leaf has-children menu-mlid-4292"><a href="/about/international-oxford">International Oxford</a></li>
<li class="leaf has-children menu-mlid-1364"><a href="/about/developing-oxford">Developing Oxford</a></li>
<li class="last leaf menu-mlid-1372"><a href="http://www.ox.ac.uk/about_the_university/jobs/index.html" title="">Jobs</a></li>
</ul></li>
</ul>

  



  
</nav>

<nav  id="block-menu-block-2" class="block block-menu-block oxweb-primary-menu-block homepage-role-base-menu block-menu-block-2 " role="navigation">
  
      
  <ul><li class="first leaf has-children menu-mlid-3382"><a href="/staff" title="Staff Gateway">Staff</a></li>
<li class="leaf has-children menu-mlid-2405"><a href="/students">Oxford students</a></li>
<li class="leaf menu-mlid-1112"><a href="https://www.alumni.ox.ac.uk/" title="">Alumni</a></li>
<li class="leaf has-children menu-mlid-2501"><a href="/visitors">Visitors</a></li>
<li class="last leaf has-children menu-mlid-2508"><a href="/local-community">Local community</a></li>
</ul>

  



  
</nav>

<div  id="block-google-appliance-ga-block-search-form" class="block block-google-appliance block-google-appliance-ga-block-search-form ">
  
      
  
  <form action="/contact-us" method="post" id="google-appliance-block-form" accept-charset="UTF-8" role="form"><div class="container-inline">
      <h2 class="element-invisible">Search Google Appliance</h2>
    <div class="form-item form-type-textfield form-item-search-keys">
  <label class="element-invisible" for="edit-search-keys">Enter the terms you wish to search for. </label>
 <input type="text" id="edit-search-keys" name="search_keys" value="" size="30" maxlength="128" class="form-text" />
</div>
<div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="Search" class="form-submit" /></div><input type="hidden" name="form_build_id" value="form-vEoX3amwGTvFJWR0lQ9cG1rOJdsVB2_2893uw9q31Ks" />
<input type="hidden" name="form_id" value="google_appliance_block_form" />
  
</div>
</form>
  </div>
  
          </div>
                  </div>
      </div>
    </div>
  </header>
  <section id="page-content" class="page-level page-content">
    <div class="wrapper">
      <div class="row space-header">

                    
        <section class="page-content-level column page-content-main" id="page-content-main">        
          
                    <section class="page-content-container content-meta" id="content-meta">
                        
    
<div  id="block-block-27" class="block block-block block block-sharebar contextual-links-region block-sharebar-sharebar-social-buttons block-block-27 ">
  
        <h2 class="title">Share This</h2>
    
  
  <!--googleoff: index--><div id="custom-tweet-button">
  <a href="https://twitter.com/share" target="_blank">Tweet</a>
</div>
<div id="custom-fb-button">
  <a href="https://www.facebook.com/sharer/sharer.php" target="_blank">Share on Facebook</a>
</div>
<div id="custom-linkedin-button">
  <a href="https://www.linkedin.com/shareArticle?mini=true" target="_blank">Share on LinkedIn</a>
</div>
<div id="custom-reddit-button">
  <a href="//www.reddit.com/submit" onclick="window.open('//www.reddit.com/submit?url='+encodeURIComponent(window.location)); return false">Share on Reddit</a>
</div>
<script>
<!--//--><![CDATA[// ><!--
(function ($) {
  var fblink = $('#custom-fb-button a').attr('href'); 
  $('#custom-fb-button a').attr('href', fblink + '?u=' + encodeURIComponent(location.href));
  var linkedinlink = $('#custom-linkedin-button a').attr('href'); 
  $('#custom-linkedin-button a').attr('href', linkedinlink + '&url=' + encodeURIComponent(location.href) + '&title=' + encodeURIComponent(document.title));
}(jQuery));
//--><!]]>
</script><!--googleon: index-->
  </div>
  
          </section>
                    
          <section class="page-content-container main-content" id="main-content">
                        <section id="breadcrumb-wrapper" class="page-level breadcrumb-wrapper">
              <div class="wrapper">
                <div class="row">
                  <div class="breadcrumb"><span class='breadcrumb-link breadcrumb-depth-0 breadcrumb-even breadcrumb-first'><a href="/">Home</a></span><span class='breadcrumb-link breadcrumb-depth-1 breadcrumb-odd breadcrumb-last'>Contact us</span></div>
                </div>
              </div>
            </section>
            
                                    
            <header class="main-title" id="main-title">
                                            <h1>Contact us</h1>
                                        </header>
                        
    <div  about="/contact-us" typeof="sioc:Item foaf:Document" class="ds-1col node node-page node-promoted view-mode-oxweb_full_content clearfix">

  
  

<div class="field field-name-field-body field-type-text-with-summary field-label-hidden">
  
  
                        <span class="field-item-single"><p>University of Oxford<br /> University Offices<br /> Wellington Square<br /> Oxford<br /> OX1 2JD<br /> United Kingdom</p><p>Telephone: +44 1865 270000<br /> Fax: +44 1865 270708</p>
<p>The University of Oxford is not a campus university and our colleges, departments and other constituent units are to be found throughout the city of Oxford, rather than on one central site. Departmental and college addresses and phone numbers may be found on individual <a href="//www.ox.ac.uk/about/colleges">college</a> and <a href="//www.ox.ac.uk/about/divisions-and-departments">departmental</a> websites.</p>
<p><strong>If you have a question you would like to ask</strong>, including admission queries, please use our “<a href="http://uni-of-oxford.custhelp.com/">Any Questions</a>” website. You can search popular questions or submit a question using the “Ask a question” tab.</p>
<p>If you have an issue or feedback relating to the University of Oxford <strong>website</strong> itself, please contact the <a href="mailto:webmaster@ox.ac.uk">webmaster</a>.</p></span>
        </div>
<!--[livery marker]--></div>

  
          </section>

          <div class="row">
                                    <section class="page-content-level column page-content-sidebar-second" id="page-content-sidebar-second">
                            
    
<div  id="block-block-42" class="block block-block sidebar-block block-block-42 ">
  
      
  
  <h2>CAN'T FIND WHAT YOU'RE LOOKING FOR?</h2><p>Try our extensive database of FAQs or submit your own question...</p><p><a class="any-questions-button" href="https://uni-of-oxford.custhelp.com/app/home/p/31/">Ask a question</a></p>
  </div>
  
            </section>
                      </div>

                    <section class="page-content-container post-content" id="post-content">
                        
    
<div  id="block-block-32" class="block block-block block block-sharebar contextual-links-region block-sharebar-sharebar-social-buttons share-bar-responsive block-block-32 ">
  
        <h2 class="title">Share This</h2>
    
  
  <div id="custom-tweet-button">
  <a href="https://twitter.com/share" target="_blank">Tweet</a>
</div>
<div id="custom-fb-button">
  <a href="https://www.facebook.com/sharer/sharer.php" target="_blank">Share on Facebook</a>
</div>
<div id="custom-linkedin-button">
  <a href="https://www.linkedin.com/shareArticle?mini=true" target="_blank">Share on LinkedIn</a>
</div>
<div id="custom-reddit-button">
  <a href="//www.reddit.com/submit" onclick="window.open('//www.reddit.com/submit?url='+encodeURIComponent(window.location)); return false">Share on Reddit</a>
</div>
<script>
<!--//--><![CDATA[// ><!--
(function ($) {
  var fblink = $('#custom-fb-button a').attr('href'); 
  $('#custom-fb-button a').attr('href', fblink + '?u=' + encodeURIComponent(location.href));
  var linkedinlink = $('#custom-linkedin-button a').attr('href'); 
  $('#custom-linkedin-button a').attr('href', linkedinlink + '&url=' + encodeURIComponent(location.href) + '&title=' + encodeURIComponent(document.title));
}(jQuery));
//--><!]]>
</script>
  </div>
  
          </section>
                  </section>
      </div>
    </div>
  </section><!--/#page-content-->

  <footer id="page-footer" class="page-level page-footer">
    <div class="wrapper">
      <div class="row">
                        
    
<div  id="block-block-15" class="block block-block social-links block-block-15 ">
  
      
  
  <h2>Connect with us</h2>
<ul class="social"><li><a class="itunes" href="//www.ox.ac.uk/itunes-u">iTunes</a></li>
  <li><a class="youtube" href="http://www.youtube.com/oxford">Youtube</a></li>
  <li><a class="facebook" href="https://www.facebook.com/the.university.of.oxford">Facebook</a></li>
  <li><a class="twitter" href="https://twitter.com/uniofoxford">Twitter</a></li>
  <li><a class="linkedin" href="https://www.linkedin.com/company/4477?trk=prof-exp-company-name">LinkedIn</a></li>
  <li><a class="weibo" href="http://e.weibo.com/OxfordUni">Weibo</a></li>
  <li><a class="oxford-apps" href="//www.ox.ac.uk/apps">Oxford Applications</a></li>
  <li><a class="instagram" href="http://instagram.com/oxford_uni">Instagram</a></li>
</ul>
  </div>

<div  id="block-block-14" class="block block-block site-map block-block-14 ">
  
      
  
  <div class="sitemap-item"><h2>Information About</h2><ul><li><a href="//www.ox.ac.uk/about/organisation">Oxford University</a></li><li><a href="//www.ox.ac.uk/about/organisation/strategic-plan">Strategic plan</a></li><li><a href="//www.ox.ac.uk/research">Oxford's research</a></li><li><a href="//www.ox.ac.uk/node/1783/">Fees and funding</a></li><li><a href="//www.ox.ac.uk/research/libraries">Libraries</a></li><li><a href="//www.ox.ac.uk/visitors/visiting-oxford/visiting-museums-libraries-places">Museums and collections</a></li><li><a href="//www.ox.ac.uk/admissions/undergraduate/open-days-outreach/open-events-and-visiting/university-open-days">Open days</a></li><li><a href="//www.ox.ac.uk/about/organisation/history/oxford-glossary">Oxford glossary</a></li><li><a href="http://www.sport.ox.ac.uk/">Sport at Oxford</a></li><li><a href="http://www.conference-oxford.com/index.php">Conferences at Oxford</a></li></ul></div><div class="sitemap-item"><h2>Information For</h2><ul><li><a href="//www.ox.ac.uk/admissions/undergraduate">Prospective undergraduates</a></li><li><a href="//www.ox.ac.uk/admissions/graduate">Prospective graduate students</a></li><!-- <li><a href="//www.ox.ac.uk/admissions/undergraduate/international-students">International students</a></li>--><li><a href="//www.ox.ac.uk/admissions/continuing-education">Prospective&nbsp;Continuing Education&nbsp;students</a></li><li><a href="//www.ox.ac.uk/admissions/continuing-education/online-and-distance-courses">Prospective online/distance learning students</a></li><li><a href="//www.ox.ac.uk/students">Current Oxford students</a></li><li><a href="//www.ox.ac.uk/staff">Current Oxford staff</a></li><li><a href="//www.ox.ac.uk/local-community">Oxford residents/Community</a></li><li><a href="//www.ox.ac.uk/visitors">Visitors/Tourists</a></li><li><a href="//www.ox.ac.uk/news-and-events">Media</a></li><li><a href="https://www.alumni.ox.ac.uk/">Alumni</a></li><li><a href="//www.ox.ac.uk/admissions/undergraduate/open-days-outreach">Teachers</a></li><li><a href="//www.ox.ac.uk/oxford-in-westminster">Parliamentarians</a></li><li><a href="http://partnership.ox.ac.uk/">Businesses/Partnerships</a></li></ul></div><div class="sitemap-item"><h2>Quick Links</h2><ul><li><a href="//www.ox.ac.uk/gsearch/">Contact search</a></li><li><a href="//www.ox.ac.uk/about_the_university/jobs/index.html">Jobs and vacancies</a></li><li><a href="//www.ox.ac.uk/about/facts-and-figures/dates-of-term">Term dates</a></li><li><a href="//www.ox.ac.uk/visitors/map">Map</a></li><li><a href="https://owa.nexus.ox.ac.uk/">Nexus webmail</a></li><li><a href="http://www.campaign.ox.ac.uk">Giving to Oxford</a></li><li><a href="//www.ox.ac.uk/public-affairs/social-media-hub">Social Media Hub</a></li><li><a href="http://www.oxforduniversityimages.com/">Oxford University Images</a></li></ul></div>
  </div>

<div  id="block-block-16" class="block block-block legals-questions block-block-16 ">
  
      
  
  <ul><li class="copyright">
  ©  University of Oxford 2016
  </li>  
  <li>
    <a href="//www.ox.ac.uk/contact-us">Contact us</a>
  </li>  
  <li>
    <a href="//www.ox.ac.uk/about-this-site">About this site</a>
  </li>  
  <li>
    <a href="//www.ox.ac.uk/legal">Legal</a>
  </li>  
  <li>
    <a href="http://www.admin.ox.ac.uk/councilsec/compliance/dataprotection/privacypolicy/">Privacy policy</a>
  </li> 
  <li>
    <a href="//www.ox.ac.uk/content/cookie-statement">Cookie statement</a>
  </li> 
 
</ul>
  </div>

<div  id="block-block-237" class="block block-block block-block-237 ">
  
      
  
  <script type="text/javascript">
<!--//--><![CDATA[// ><!--

  _bizo_data_partner_id = "9293";

//--><!]]>
</script><script type="text/javascript">
<!--//--><![CDATA[// ><!--

(function() {
  var s = document.getElementsByTagName("script")[0];
  var b = document.createElement("script");
  b.type = "text/javascript";
  b.async = true;
  b.src = (window.location.protocol === "https:" ? "https://sjs" : "http://js") + ".bizographics.com/insight.min.js";
  s.parentNode.insertBefore(b, s);
})();

//--><!]]>
</script><noscript>
  <img height="1" width="1" alt="" style="display:none;" src="//www.bizographics.com/collect/?pid=9293&amp;fmt=gif" /></noscript>
  </div>
  
      </div>
    </div>
  </footer>
  </section>
  
    </body>
</html>


"""

addresses = c.extract(html)
print addresses
