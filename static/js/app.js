// Replace with your own values
const searchClient = algoliasearch(
  'FC0U9GZK78',
  '5644c7154a9efaa946d3221c7c908062' // search only API key, not admin API key
);

const search = instantsearch({
  indexName: 'contacts',
  searchClient,
  routing: true,
});

search.addWidgets([
  instantsearch.widgets.configure({
    hitsPerPage: 10,
  })
]);

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#search-box',
    placeholder: 'Search for contacts',
  })
]);

search.addWidgets([
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: `We didn't find any results for the search <em>"{{query}}"</em>`,
    },
  })
]);

search.start();
