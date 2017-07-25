
function changeIFrame() 
{
	document.getElementById("mySpan").innerHTML = '[' + urlsIdx + '][' + urls[urlsIdx] + ']';
	document.getElementById('myIframe').src = urls[urlsIdx];			
}

function anteriorClick() 
{
	urlsIdx = urlsIdx - 1;
	if(urlsIdx < 0) 
	{
		urlsIdx = 0;
	}
	if(urlsIdx == 0) 
	{
		document.getElementById('btnAnterior').disabled = true;
	}
	document.getElementById('btnSiguiente').disabled = false;
	changeIFrame();
}

function siguienteClick() 
{
	urlsIdx = urlsIdx + 1;
	if(urlsIdx > (urls.length - 1)) 
	{
		urlsIdx = (urls.length - 1);
	}
	if(urlsIdx == (urls.length - 1)) 
	{
		document.getElementById('btnSiguiente').disabled = true;
	}
	document.getElementById('btnAnterior').disabled = false;
	changeIFrame();
}

function eliminarClick() 
{
	urls[urlsIdx] = '';
	changeIFrame();
}			

function imprimirClick() 
{
	var html = '';
	for(var i=0; i<urls.length; i++) 
	{
		html = html + "'" + urls[i] + "',<br/>";
	}
	document.getElementById("mySpan").innerHTML = html;
}
