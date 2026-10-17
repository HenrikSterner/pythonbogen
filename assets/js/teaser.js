(() => {
  const video = document.querySelector('.teaser-film-stage video');
  const playButton = document.querySelector('.film-play');
  if (video && playButton) {
    playButton.hidden = false;
    playButton.addEventListener('click', async () => {
      playButton.hidden = true;
      try {
        await video.play();
        video.focus();
      } catch {
        playButton.hidden = false;
      }
    });
    video.addEventListener('play', () => { playButton.hidden = true; });
    video.addEventListener('ended', () => { playButton.hidden = false; });
  }
  const dialog = document.querySelector('#smagsproeve');
  if (!dialog) return;
  document.querySelectorAll('[data-open-sample]').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      dialog.showModal();
      dialog.scrollTop = 0;
      document.body.classList.add('sample-is-open');
    });
  });
  dialog.querySelector('[data-close-sample]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => document.body.classList.remove('sample-is-open'));
  dialog.addEventListener('click', event => {
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
})();
