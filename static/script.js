console.log("We're on");

const getResults = async () => {
  const data = await fetch("/results");
  const json = await data.json();
  console.log(json);
  return json;
};

getResults();
