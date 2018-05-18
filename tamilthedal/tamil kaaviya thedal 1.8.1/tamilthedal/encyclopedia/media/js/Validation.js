
function ReqValidate(controls,fileds)
{
    controlname = controls.split(',');
	filedname  = fileds.split(',');
	len = controlname.length;
	for (var i=0;i<	len;i++)
	{
		value = document.getElementById(controlname[i]).value;
		if(value == '')
		{
			alert(filedname[i] +' should not be empty.');
			document.getElementById(controlname[i]).focus();
			return false;
		}
		if (value.indexOf(' ') == 0)
	{       
			alert('prefix space not allowed in '+ filedname[i]);
			return false;
		
    }
}
	return true;
}

/* Change password java script */
function validatePwd() {
 
    var invalid = " "; // Invalid character is a space
    var minLength = 6; // Minimum length    
    var pw1 = document.getElementById("password").value;
    var pw2 = document.getElementById("retypepassword").value;
    var re = /^\w*(?=\w*\d)(?=\w*[a-zA-Z]\w*$)/
                
    // check for a value in both fields.
    if (pw1 == '' || pw2 == '') {
    alert('Please enter your password twice.');
    return false;
    }
    // check for minimum length
    if (document.getElementById("password").value.length < minLength) {
    alert('Your password must be at least ' + minLength + ' characters long.');
    return false;
    }
    // check for spaces
    if (document.getElementById("password").value.indexOf(invalid) > -1) {
    alert("Sorry, spaces are not allowed.");
    return false;
    }
    realphanumeric= /[a-z]/;
    realalphanumeric = /[A-Z]/; 
	if (!realphanumeric.test(pw1) && !realalphanumeric.test(pw1)){
        
		alert("The password must contain at least one letter!"); 
		return false; } 
	realphanumeric= /[0-9]/; 
	if (!realphanumeric.test(pw1)){
		alert("The password must contain at least one number!"); 
		return false; } 
    else{
	if (!re.test(pw1)){
        alert("The password should not contain special characters.");
       return false;}
        
    else{
    if (pw1 != pw2) {
        alert ("The passwords you entered does not match.");
        return false;}
        
    else
    return true;
          }
		  }
       }


       
function getComboValue(controls,fields)
{
   
    controlname = controls.split(',');
	filedname  = fields.split(',');
	len = controlname.length;
	for (var i=0;i<	len;i++)
	{
		if(document.getElementById(controlname[i]).value != '')
		{
	     //alert(document.getElementById(controlname[i]).value);
	     document.getElementById(filedname[i]).value = document.getElementById (controlname[i]).value;
        }
    }
}
       
function ComboValidate(controls,fields)
{
	controlname = controls.split(',');
	fieldname  = fields.split(',');
	len = controlname.length;	

	for (var i=0;i<	len;i++)
	{
		if(document.getElementById(controlname[i]).value == ''||document.getElementById(controlname[i]).value == '0')
		{
			alert('please select '+fieldname[i]+'.');
			return false;
		}
	}
	return true;	
}
function checkboxvalidate(check1) {
chk1 = document.getElementById(check1);
alert('ch1'+ chk1);
if(chk1.checked == false || chk1.checked ==0)
{
    alert('Select your event');
    return false;
}
else 
return true;

} 


function dateMask(input)
{	
   format = formatDate();
	if (format == 'm-d-Y'){
		dateFormat = 'mm-dd-yyyy';
	}
	if (format == 'd-m-Y'){
		dateFormat = 'dd-mm-yyyy';
	}
	if (format == 'Y-m-d'){
		dateFormat = 'yyyy-mm-dd';
	}
   if (document.getElementById(input).value == '' || document.getElementById(input).value == '2000-01-01')
   {
   	
   	document.getElementById(input).value = dateFormat;
   }
}

function dateClean(textin){
  if (document.getElementById(textin) == null)
	return;  
 if(document.getElementById(textin).value == "mm-dd-yyyy" || document.getElementById(textin).value == "dd-mm-yyyy" || document.getElementById(textin).value == "yyyy-mm-dd")
	{
		document.getElementById(textin).value = '';
	}
}

function confirmation(check1,check2,check3)
{	
//    chk1 = document.getElementById(check1);
//    chk2 = document.getElementById(check2);
//    chk3 = document.getElementById(check3);
//	 if((chk1.checked == false || chk1.checked ==0)&&(chk2.checked == false || chk2.checked ==0)&&(chk3.checked == false || chk3.checked ==0))
//	 {
//	    alert("Select a checkbox to associate email address");
//	        return false;
//	 }
//	 else
//	    return true;
	 
}
function deleteconfirmation(chk)
{		
    if(chk.length !=null)
    {
		
        var checked= 0
        for (i = 0; i < chk.length; i++)
        {
       
	        if(chk[i].checked == true )
	        {
	          checked =1 ;
		      return confirm("Are you sure you want to delete?")
	        }
    	   
	     }	    
	 }
	 if(chk.checked == false || checked ==0)
	 {
	    alert("select a record to delete");
	        return false;
	 }
	 else
	    return confirm("Are you sure you want to delete?")
	 
}

function addconfirmation(chk)
{	
	
    if(chk.length !=null)
    {
        var checked= 0
        for (i = 0; i < chk.length; i++)
        {
			
	        if(chk[i].checked == true )
	        {
	          checked =1 ;
		      return true;
	        }
    	   
	     }	    
	 }
	 if(chk.checked == false || checked ==0)
	 {
	    
	        return false;
	 }
	 else
	    return true;
	 
}

function assignconfirmation(chk)
{	
	alert(chk.length);
    if(chk.length !=null)
    {
        var checked= 0
        for (i = 0; i < chk.length; i++)
        {
       
	        if(chk[i].checked == true )
	        {
	          checked =1 ;
		      return true;
	        }
    	   
	     }	    
	 }
	 if(chk.checked == false || checked ==0)
	 {
	    
	        return false;
	 }
	 else
	    return true;
	 
}

function sendconfirmation(chk)
{	
	
    if(chk.length !=null)
    {
		var check= 0
        for (i = 0; i < chk.length; i++)
        {
			if(chk[i].checked == true )
	        {
			  check =1 ;
		      return true;
	        }
    	   
	     }	    
	 }
	 
	 if(chk.checked == false || check ==0)
	 {
		
	   
	        return false;
	 }
	 else
	    return true;
	 
}

function doCheck(strForm)
{
  if(strForm)
	{
        objForm = document.getElementById(strForm);
	
        for(i=0; i < objForm.elements.length; i++)
		{
            if(objForm.elements[i].type == "checkbox")
			{
	            if(objForm.elements[i].checked == false)
				{
			
                	objForm.elements[i].checked = true;
				}
                	
			}
			   		
    	}
	}

}




function unCheck(strForm)
{
  if(strForm)
	{
        objForm = document.getElementById(strForm);
	
        for(i=0; i < objForm.elements.length; i++)
		{
            if(objForm.elements[i].type == "checkbox")
			{
	            if(objForm.elements[i].checked == true)
				{
			
                	objForm.elements[i].checked = false;
				}
                	
			}
			   		
    	}
	}

}

function urlValidation(controls,fileds)
{
    
	controlname = controls.split(',');	
	filedname  = fileds.split(',');	
	len = controlname.length;	
	for (var i=0;i<	len;i++)
	{	    
        var filter = '';//^([\w]+:\w+@)?(([a-zA-Z]{1}([\w\-]+\.)+([\w]{2,5}))(:[\d]{1,5})?)?((/?\w+/)+|/?)(\w+\.[\w]{3,4})?([,]\w+)*((\?\w+=\w+)?(&\w+=\w+)*([,]\w*)*)?/;
        if(!(filter.test(document.getElementById(controlname[i]).value)))
		{
			alert(filedname[i] +' should have valid URL.');
			return false;
		}		
    }
    return true;
}
    
function emailValidation(controls,fields)
{    
	

	controlname = controls.split(',');	
	filedname  = fields.split(',');	
	len = controlname.length;	
	for (var i=0;i<	len;i++)
	{
		if(document.getElementById(controlname[i]).value.length ==0){
			return true;
		}	    
	    var filter = /^[a-zA-Z][\w\.-]*[a-zA-Z0-9]@[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z]$/;
		if(!(filter.test(document.getElementById(controlname[i]).value)))
		{
			alert(fieldname[i] +' should have valid email address.');
			return false;
		}		
	}
	return true;
}

function getDatewedding(obj){
    //dd/mm/yyyy
    var strDate = document.getElementById(obj).value;     
    if(strDate.length >=10){
        var dateObj = strDate.split('-');
     }
    var dateValue = new Date();
    dateValue.setFullYear(dateObj[2],((dateObj[0])-1),dateObj[1]);
    return dateValue;
}




function gettime(obj)
{
var startmeeting = document.getElementById(obj).value;
startm = startmeeting.split(' ');
time = startm[0];
ampm= startm[1];

times = time.split(':');
hours = times[0];
minutes = times[1];
if(ampm == 'PM')
{
if(hours != 12)
{
hours = parseInt(hours) + 12;
}
}

return {hours:hours,minutes:minutes};
}




function checkdate(objName) 
{
var datefield = objName;
if (chkdate(objName) == false)
{
datefield.select();
alert("date is invalid.");
datefield.focus();
return false;
}
else {
return true;
   }
}



function fromToDateCheck(from,to){    
    var valid = false;
    if(document.getElementById(from)==null)
        return true;
        
    fromDate = getDate(from);
    toDate = getDate(to);
    if (Date.parse(fromDate) > Date.parse(toDate)) {
        valid = false;
        alert ("Start date should be greater than the end date.");
        }
    else {
        valid = true;
    }
     
   return valid;   
}

function plannedActualDateCheck(planned,actual){    
    var valid = false;
	if(document.getElementById(planned)==null)
        return true;
    var plannedDate = getDate(planned);
    var actualDate = getDate(actual);
    if (Date.parse(plannedDate) > Date.parse(actualDate)) {
        valid = false;
        alert ("Actual date should be within the planned date.");
        }
    else {
        valid = true;
    }
   return valid;   
}

function TaskDateCheck(planned,actual){    
    var valid = false;
	if(document.getElementById(planned)==null)
        return true;
    var plannedDate = getDate(planned);
    var actualDate = getDate(actual);
    if (Date.parse(plannedDate) > Date.parse(actualDate)) {
        valid = false;
        alert ("Task date should be within the program date.");
        }
    else {
        valid = true;
    }
   return valid;   
}

function DateCheck(planned,actual,start,end,action){    
    var valid = false;
	if(document.getElementById(planned)==null)
        return true;
    var plannedDate = getDate(planned);
    var actualDate = getDate(actual);
    if (Date.parse(plannedDate) > Date.parse(actualDate)) {
        valid = false;
        alert (start +' should not be '+ action + ' than ' +end);
        }
    else {
        valid = true;
    }
   return valid;   
}

function getDate(obj){
    //mm/dd/yyyy
    var strDate = document.getElementById(obj).value;	

    if(strDate.length >=10){
       var dateObj = strDate.split('-');
     }
    alert(dateObj[2]+dateObj[1]+dateObj[0])
    var dateValue = new Date();
    dateValue.setFullYear(dateObj[2],dateObj[1],dateObj[0]);  
    return dateValue;
}

function divcontentclass()
{

    if (document.getElementById('maincontent') != null)
    {
        if (navigator.appName == "Microsoft Internet Explorer")
        {
           document.getElementById('maincontent').className='wr-arIE';
        }
        else
        {
            document.getElementById('maincontent').className='wr-ar';
        }
    }
}

function browserbasedcss()
{    
    if (document.getElementById('rightmenu') != null)
    {
        if (navigator.appName == "Microsoft Internet Explorer")
        {
            document.getElementById('rightmenu').className='wr-sideIE';
            var i=1;
            for (i=1;i<=5;i++)
            {
                document.getElementById('About'+i).className='divothermenu';
                document.getElementById('CompanyInfo'+i).className='divmainmenu';
                document.getElementById('Bride'+i).className='divothermenu';
                document.getElementById('Vendorlogin'+i).className='divothermenu';
                document.getElementById('Contact'+i).className='divothermenu';
            }
        }
        else
        {
            document.getElementById('rightmenu').className='wr-side';
            var i = 1;
             for (i=1;i<=5;i++)
            {
                document.getElementById('About'+i).className='divothermenu';
                document.getElementById('CompanyInfo'+i).className='divothermenu';
                document.getElementById('Bride'+i).className='divothermenu';
                document.getElementById('Vendorlogin'+i).className='divothermenu';
                document.getElementById('Contact'+i).className='divothermenu';
            }
        }
    }
    divcontentclass();
}
function printMe(divID,pinklogo)
{ 
  var disp_setting="toolbar=yes,location=no,directories=yes,menubar=yes,"; 
      disp_setting+="scrollbars=yes,width=650, height=600, left=100, top=25"; 
  var content_vlue = document.getElementById(divID).innerHTML; 
  var logo =  document.getElementById(pinklogo).value;

  var docprint=window.open("","",disp_setting); 
   docprint.document.open(); 
   docprint.document.write('<html><title>pinksutra.com</title><head> ');   
   docprint.document.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/m_style_verdana.css" title="standard-css1" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/m_style-s.css" title="tiny-css1" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/m_style-l.css" title="large-css1" />');
   docprint.document.write('<link href="/static/css/m_style_verdana.css" rel="stylesheet" type="text/css" />');
   docprint.document.write('<link href="/static/css/forms.css" rel="stylesheet" type="text/css" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/container.css" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/contract.css" />');
   docprint.document.write('<link href="/static/css/project_dashboard.css" rel="stylesheet" type="text/css" media="screen" /> </link>');   
   docprint.document.write('</head><body onLoad="self.print()"><center>');
   docprint.document.write('<img src=' );   
   docprint.document.write(logo);
   docprint.document.write('>');         
   docprint.document.write(content_vlue);
docprint.document.write('<span class="con-pink">powered by www.pinksutra.com</span>');        
   docprint.document.write('</center></body></html>'); 
   docprint.document.close(); 
   docprint.focus(); 
}

function responsibilityCardPrint(divID)
{ 
  var disp_setting="toolbar=yes,location=no,directories=yes,menubar=yes,"; 
      disp_setting+="scrollbars=yes,width=650, height=600, left=100, top=25"; 
  var content_vlue = document.getElementById(divID).innerHTML;
  var name =  document.getElementById("weddingTeamMemberName").value;
  var logo =  document.getElementById("logo").value;
  
  var docprint=window.open("","",disp_setting); 
   docprint.document.open(); 
   docprint.document.write('<html><title>pinksutra.com</title><head> ');   
   docprint.document.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/m_style_verdana.css" title="standard-css1" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/m_style-s.css" title="tiny-css1" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/m_style-l.css" title="large-css1" />');
   docprint.document.write('<link href="/static/css/m_style_verdana.css" rel="stylesheet" type="text/css" />');
   docprint.document.write('<link href="/static/css/forms.css" rel="stylesheet" type="text/css" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/container.css" />');
   docprint.document.write('<link rel="stylesheet" type="text/css" href="/static/css/contract.css" />');
   docprint.document.write('<link href="/static/css/project_dashboard.css" rel="stylesheet" type="text/css" media="screen" /> </link>');   
   docprint.document.write('</head><body onLoad="self.print()"><center>');
   docprint.document.write('<img src=' );   
   docprint.document.write(logo);
   docprint.document.write('></center>');
   docprint.document.write('<span class="con-pink" style="font-size:16px;padding-left:10px">responsibility card for ');
   docprint.document.write(name);
   docprint.document.write('</span><br><br><span style="padding-left:10px">make sure you print this card and bring it with you on the day of this event. - Thanks</span>');
   docprint.document.write(content_vlue);
   docprint.document.write('<center><span class="con-pink">powered by www.pinksutra.com</span></center>');
   docprint.document.write('</body></html>'); 
   docprint.document.close(); 
   docprint.focus(); 
}


function convertDate(obj)
{
  if (document.getElementById(obj) == null)
	return;  
   dateVal = document.getElementById(obj).value ;

   if( dateVal != '')
   {                      
        frmt = formatDate();
	frmtVal = frmt.split('-');
	var m =''; // to represent the month index
	var d = ''; // to represent the day index
	var y = ''; // to represent the year index			
	if ((dateVal.split("-")[0]).length > 2 )
	{
		y = 0;
		m = 1;
		d = 2;
	}		
	else if(frmtVal[0]=='m')
	{
		m=0;
		d=1;
		y=2;	
 	}
	else
	{
		d=0;
		m=1;
		y=2;			
	}
	var yearfield=dateVal.split("-")[y];
	var monthfield = dateVal.split("-")[m];
	var dayfield = dateVal.split("-")[d];

	daytimefield = dayfield.split(' ')
	if (daytimefield.length > 0)
		dayfield = daytimefield[0]
	var day = new Date(yearfield, monthfield-1, dayfield);	
        document.getElementById(obj).value = day.strfdate(frmt);
	
   }
}

function isDate(value){
if(value.length==0){
	return true; }
if(value.length < 10){
	return false; }
if(value.length > 10){
	return false; }
var returnval = false;
if(value.indexOf(' ') == 0)
	return false	
		var monthfield = '';
		var dayfield = '';
		
		frmt = formatDate();
		frmtVal = frmt.split('-');		
		if(frmtVal[0]=='m'){	
			monthfield=value.split("-")[0];
		 	dayfield=value.split("-")[1]; }
		else{
				dayfield=value.split("-")[0];
				monthfield=value.split("-")[1]; }
		var yearfield=value.split("-")[2];
				
		var dayobj = ''
		try {		
			dayobj = new Date(yearfield, monthfield-1, dayfield);			
			if ((dayobj.getMonth()+1!=monthfield)||(dayobj.getDate()!=dayfield)||(dayobj.getFullYear()!=yearfield))
				returnval = false;
		else
		returnval=true;
			 }
		catch(err){			
			returnval = false;
		}
	return returnval;
}

function isBetweenDate(fromDt,toDt){    
    var valid = false;
	if(fromDt == null)
        return true;
   if( toDt == null)
        return true;
   frmt = formatDate();
	frmtVal = frmt.split('-');
	var monthfield =''
	var dayfield = ''
	var tomonthfield =''
	var todayfield = ''
			
	if(frmtVal[0]=='m'){	
			monthfield = fromDt.split("-")[0];
		 	dayfield = fromDt.split("-")[1];
		 	tomonthfield = toDt.split("-")[0];
		 	todayfield = toDt.split("-")[1]; 
		 	}
	else{
			dayfield=fromDt.split("-")[0];
			monthfield=fromDt.split("-")[1];
			tomonthfield = toDt.split("-")[1];
		 	todayfield = toDt.split("-")[0];  
			}
	var yearfield=fromDt.split("-")[2];
	var toyearfield=toDt.split("-")[2];
				
	var fromDay = new Date(yearfield, monthfield-1, dayfield);	
	var toDay = new Date(toyearfield, tomonthfield-1, todayfield);
      
    if (fromDay > toDay) {
        valid = false;        
        }
    else {
        valid = true;
    }
   return valid;   
}

function isNumeric(value) {
  if (value == null || !value.toString().match(/^[-]?\d*\.?\d*$/)) return false;
  return true;
}

function isContactNum(value) {
  if (value == null || !value.toString().match(/^[-+]?\d*$/)) return false;
  return true;
}



function isZipCode(value){
	if (value == null || !value.toString().match(/(^\d*$)|(^\d{5}(-\d{4})?$)|(^[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}$)/)) return false;
	return true;
}


  function getcity(event)
{

            var form = this;
            var data = {}

           getdata = $("#state").val()    

$.getJSON("/getcity/?stateid="+getdata, 
function(json)
{

document.getElementById('city').options.length =0;
if (json.length > 0)
{
	for (j =json.length-1 ;j >=0;j--)
	{
	  if ((/Firefox[\/\s](\d+\.\d+)/.test(navigator.userAgent))||(navigator.appName == "Microsoft Internet Explorer" ))
	  {
	    newLi = $('<option selected value='+json[j].id+'>'+json[j].name+'</option>');
		$("#city").prepend(newLi);
	  }
	  else
	  {
	    newLi = $('<option value='+json[j].id+'>'+json[j].name+'</option>');
		$("#city").prepend(newLi);
	  }
	  
	  
	}
}

	var newLi = $('<option selected="selected" value= "0" >select</option>');
	$("#city").prepend(newLi);

 }
);

}

function CheckKeyCode(e) {
    if (navigator.appName == "Microsoft Internet Explorer") {
        if ((e.keyCode >= 48 && e.keyCode <= 57) || (e.keyCode == 45) || (e.keyCode == 127) || (e.keyCode == 8))
        { return true; }
        else
        { return false; } 
    }
    else {
        if ((e.charCode >= 48 && e.charCode <= 57) || (e.charCode == 45) || (e.charCode == 127) || (e.charCode == 0))
        { return true; }
        else
        { return false; } 
    }
}