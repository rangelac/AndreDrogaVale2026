# André da Droga Vale — Eleições 2026

Site estático em português com identidade visual fornecida pela campanha, biografia, linha do tempo, atuação parlamentar documentada e contato pelo Instagram.

## Publicação

O diretório público é `dist/`. Ele contém todos os arquivos necessários e pode ser publicado em hospedagem estática, inclusive na Hostinger. Não exige instalação de dependências nem servidor de aplicação. Ao importar o repositório, escolha `dist` como diretório público; alternativamente, copie o conteúdo de `dist` para `public_html`.

Domínio solicitado: https://andredrogavale11444.com.br/

O registro do domínio, a hospedagem pública e os apontamentos DNS precisam estar configurados para esse endereço funcionar. A prévia privada no Sites não configura automaticamente esse domínio.

## Conteúdo e revisão

- `dist/index.html`: texto, links e metadados.
- `dist/styles.css`: identidade visual e adaptação a telas menores.
- `dist/refinement.css`: refinamento tipográfico, composição da abertura e ritmo de espaçamentos.
- `dist/assets/fonts/`: fonte variável Manrope hospedada localmente e licença SIL Open Font License.
- `dist/script.js`: menu móvel e aviso de privacidade.
- `dist/assets/`: versões otimizadas dos materiais fornecidos, sem alteração da identidade ou da foto.
- `FONTES.md`: referências, correções no relatório e pontos ainda não confirmados.

Não foram adicionados depoimentos inventados, números de telefone presumidos, promessas não aprovadas, perfis de eleitores, formulários ou rastreamento. O Instagram funciona como destino de contato até que a campanha forneça um WhatsApp oficial.

## Prévia local

Execute `python -m http.server 4184 --bind 127.0.0.1 --directory dist` na pasta do projeto e abra http://127.0.0.1:4184/.

## Compatibilidade

O conteúdo principal e as iniciativas funcionam sem JavaScript. Com JavaScript, há menu móvel recolhível e diálogo de privacidade. O CSS respeita a preferência por movimento reduzido. Não há dependência de fontes, bibliotecas ou rastreadores externos para renderizar a página.
