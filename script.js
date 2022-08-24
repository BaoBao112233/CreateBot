// const s = async() => {
//   const response = await fetch('https://api.covid19api.com/summary');
//   const result = await response.json();
//   return result.Global;
// };

// const n = s()
//   .then(rs => console.log(`Date: ${rs.Date}`)) 

const url = 'https://api.covid19api.com/summary'

const Global = async() => 
  fetch(url) 
  .then ((response) => response.json())
  .then ((data) => handleData(data))

// let id = `Taiwan`;

// function render(global) {
//   let g = global.Countries;
//   let print = g.map((f,i) => {
//     if (id.toLowerCase() == f.Slug){
//       var str = `Country: ${f.Country} \nNew Confirmed: ${f.NewConfirmed}`;
//       return str;
//     }
//   });
// };

function handleData(data){ 
  let pr = data['Global'];
 const html = `Date: ${pr['Date']} \nNew Confirmed: ${pr.NewConfirmed} \nTotal Confirmed: ${pr.TotalConfirmed} \nNew Deaths: ${pr.NewDeaths} \nTotal Deaths: ${pr.TotalDeaths} \nNew Recovered: ${pr.NewRecovered} \nTotal Recovered: ${pr.TotalRecovered}`;
return html.toString();
}



// function render(global) {
//   let g = global.Global
//   console.log(g.Date)
// }

// Global(render)

// const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
// //Tạo tin nhắn để gửi đi

// const url = 'https://api.covid19api.com/summary'

// const Global = async(callback) =>{
//   fetch(url) 
//   .then((response) => response.json()) 
//   .then((callback));
// };

// function render(global) {
//   let g = global.Global
//   return g;
// }

// module.exports = async (event, context) => {
//   lib.discord.channels['@0.0.6'].messages.create({
//     //Nhận diện được Server Discord để gửi tin nhắn
//     channel_id: context.params.event.channel_id,
//     content: [`${Global(render)}`].join('\n'), //Nhập nội dung tin nhắn cần gửi
//   });
// };
