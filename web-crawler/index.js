const axios = require("axios");
const fs    = require("fs");

const crawler = async function(url)
{
  let index = 0;
  while (index != 10)
  {
      await axios.get(
      `${url}/${index}`,
      {
        "headers": {
          "accept": "",
          "accept-language": "",
          "content-type": "",
          "sec-ch-ua": "",
          "sec-ch-ua-mobile": "",
          "sec-ch-ua-platform": "",
          "sec-fetch-dest": "",
          "sec-fetch-mode": "",
          "sec-fetch-site": "",
          "x-requested-with": "",
          "cookie": "",
          "Referer": "",
          "Referrer-Policy": ""
      },
        "body": null,
        "method": ""
      })
      .then(res => {
        if(res.data.data !== null){
          fs.writeFileSync(``, JSON.stringify(res.data.data));
        }
        else{
          console.log("empty response...");
        }
      })
      .catch(_err => console.log(_err))
    index = index + 1;
  }
}

crawler();
