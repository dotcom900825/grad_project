(function(){var l="0123456789abcdef";function k(r){str="";for(j=0;j<=3;j++){str+=l.charAt((r>>(j*8+4))&15)+l.charAt((r>>(j*8))&15)}return str}function m(r){nblk=((r.length+8)>>6)+1;blks=new Array(nblk*16);for(i=0;i<nblk*16;i++){blks[i]=0}for(i=0;i<r.length;i++){blks[i>>2]|=r.charCodeAt(i)<<((i%4)*8)}blks[i>>2]|=128<<((i%4)*8);blks[nblk*16-2]=r.length*8;return blks}function q(r,u){var t=(r&65535)+(u&65535);var s=(r>>16)+(u>>16)+(t>>16);return(s<<16)|(t&65535)}function h(r,s){return(r<<s)|(r>>>(32-s))}function o(z,v,u,r,y,w){return q(h(q(q(v,z),q(r,w)),y),u)}function f(v,u,A,z,r,y,w){return o((u&A)|((~u)&z),v,u,r,y,w)}function n(v,u,A,z,r,y,w){return o((u&z)|(A&(~z)),v,u,r,y,w)}function g(v,u,A,z,r,y,w){return o(u^A^z,v,u,r,y,w)}function p(v,u,A,z,r,y,w){return o(A^(u|(~z)),v,u,r,y,w)}function e(r){x=m(r);a=1732584193;b=-271733879;c=-1732584194;d=271733878;for(i=0;i<x.length;i+=16){olda=a;oldb=b;oldc=c;oldd=d;a=f(a,b,c,d,x[i+0],7,-680876936);d=f(d,a,b,c,x[i+1],12,-389564586);c=f(c,d,a,b,x[i+2],17,606105819);b=f(b,c,d,a,x[i+3],22,-1044525330);a=f(a,b,c,d,x[i+4],7,-176418897);d=f(d,a,b,c,x[i+5],12,1200080426);c=f(c,d,a,b,x[i+6],17,-1473231341);b=f(b,c,d,a,x[i+7],22,-45705983);a=f(a,b,c,d,x[i+8],7,1770035416);d=f(d,a,b,c,x[i+9],12,-1958414417);c=f(c,d,a,b,x[i+10],17,-42063);b=f(b,c,d,a,x[i+11],22,-1990404162);a=f(a,b,c,d,x[i+12],7,1804603682);d=f(d,a,b,c,x[i+13],12,-40341101);c=f(c,d,a,b,x[i+14],17,-1502002290);b=f(b,c,d,a,x[i+15],22,1236535329);a=n(a,b,c,d,x[i+1],5,-165796510);d=n(d,a,b,c,x[i+6],9,-1069501632);c=n(c,d,a,b,x[i+11],14,643717713);b=n(b,c,d,a,x[i+0],20,-373897302);a=n(a,b,c,d,x[i+5],5,-701558691);d=n(d,a,b,c,x[i+10],9,38016083);c=n(c,d,a,b,x[i+15],14,-660478335);b=n(b,c,d,a,x[i+4],20,-405537848);a=n(a,b,c,d,x[i+9],5,568446438);d=n(d,a,b,c,x[i+14],9,-1019803690);c=n(c,d,a,b,x[i+3],14,-187363961);b=n(b,c,d,a,x[i+8],20,1163531501);a=n(a,b,c,d,x[i+13],5,-1444681467);d=n(d,a,b,c,x[i+2],9,-51403784);c=n(c,d,a,b,x[i+7],14,1735328473);b=n(b,c,d,a,x[i+12],20,-1926607734);a=g(a,b,c,d,x[i+5],4,-378558);d=g(d,a,b,c,x[i+8],11,-2022574463);c=g(c,d,a,b,x[i+11],16,1839030562);b=g(b,c,d,a,x[i+14],23,-35309556);a=g(a,b,c,d,x[i+1],4,-1530992060);d=g(d,a,b,c,x[i+4],11,1272893353);c=g(c,d,a,b,x[i+7],16,-155497632);b=g(b,c,d,a,x[i+10],23,-1094730640);a=g(a,b,c,d,x[i+13],4,681279174);d=g(d,a,b,c,x[i+0],11,-358537222);c=g(c,d,a,b,x[i+3],16,-722521979);b=g(b,c,d,a,x[i+6],23,76029189);a=g(a,b,c,d,x[i+9],4,-640364487);d=g(d,a,b,c,x[i+12],11,-421815835);c=g(c,d,a,b,x[i+15],16,530742520);b=g(b,c,d,a,x[i+2],23,-995338651);a=p(a,b,c,d,x[i+0],6,-198630844);d=p(d,a,b,c,x[i+7],10,1126891415);c=p(c,d,a,b,x[i+14],15,-1416354905);b=p(b,c,d,a,x[i+5],21,-57434055);a=p(a,b,c,d,x[i+12],6,1700485571);d=p(d,a,b,c,x[i+3],10,-1894986606);c=p(c,d,a,b,x[i+10],15,-1051523);b=p(b,c,d,a,x[i+1],21,-2054922799);a=p(a,b,c,d,x[i+8],6,1873313359);d=p(d,a,b,c,x[i+15],10,-30611744);c=p(c,d,a,b,x[i+6],15,-1560198380);b=p(b,c,d,a,x[i+13],21,1309151649);a=p(a,b,c,d,x[i+4],6,-145523070);d=p(d,a,b,c,x[i+11],10,-1120210379);c=p(c,d,a,b,x[i+2],15,718787259);b=p(b,c,d,a,x[i+9],21,-343485551);a=q(a,olda);b=q(b,oldb);c=q(c,oldc);d=q(d,oldd)}return k(a)+k(b)+k(c)+k(d)}window.calcMD5=e})();