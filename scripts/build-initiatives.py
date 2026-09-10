"""Generate the three static initiative pages from documented editorial records."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'dist'
home = (PUBLIC / 'index.html').read_text(encoding='utf-8')
records = [
 dict(slug='inspecoes-com-aviso-previo', title='Inspeções com aviso prévio', category='AMBIENTE DE NEGÓCIOS', document='Projeto de Lei nº 99/2025', status='Projeto com veto registrado', kind='project',
 intro='Proposta de comunicação antecipada para inspeções em novos estabelecimentos comerciais e industriais.',
 problem='A justificativa relata visitas de fiscalização que encontram novos estabelecimentos fechados enquanto aguardam licenciamento, provocando atrasos e repetição de procedimentos.',
 action='André apresentou o PL 99/2025. O texto propõe aviso mínimo de 24 horas, com comunicação oficial pela RedeSim ou sistema equivalente, inclusive para inspeções por videoconferência.',
 situation='O Veto nº 11/2026, apresentado em 5 de maio de 2026, refere-se expressamente a este projeto. Na consulta, o cadastro do veto informa que ele está em tramitação. Esse registro é posterior ao projeto e deve ser considerado ao avaliar sua situação.',
 result='A autoria do projeto e a existência do veto estão documentadas. Não foi localizada, nas fontes consultadas, confirmação de derrubada do veto ou publicação de lei decorrente do PL 99/2025.',
 execution='Não há comprovação de execução desta proposta nas fontes consultadas. O texto do projeto, por si só, não estabelece uma obrigação vigente para os estabelecimentos ou para a fiscalização.',
 events=[('2025-07-08','8 de julho de 2025','Apresentação do PL 99/2025 no SAPL.',1),('2026-05-05','5 de maio de 2026','Apresentação do Veto nº 11/2026 ao projeto.',2),('2026-09-10','Consulta em 10 de setembro de 2026','Cadastro do veto consultado: em tramitação.',2)],
 sources=[('Texto original e justificativa do PL 99/2025','https://sapl.al.ac.leg.br/media/sapl/public/materialegislativa/2025/17508/pl-n-99-andre_vale.pdf'),('Cadastro do Projeto de Lei nº 99/2025','https://sapl.al.ac.leg.br/materia/17508'),('Cadastro do Veto nº 11/2026','https://sapl.al.ac.leg.br/materia/19337')], refs=[0,0,2,2,2]),
 dict(slug='cooperacao-vigilancia-sanitaria', title='Cooperação para serviços digitais', category='VIGILÂNCIA SANITÁRIA', document='Indicação nº 43/2025', status='Pedido formal registrado', kind='request',
 intro='Solicitação de diálogo para ampliar o uso de uma plataforma de relatórios de medicamentos.',
 problem='Segundo a justificativa, a digitalização estadual não alcançaria automaticamente as vigilâncias municipais independentes de Rio Branco, Cruzeiro do Sul e Sena Madureira.',
 action='André solicitou ao governo estadual, por meio da Sesacre, diálogo com essas prefeituras para construir cooperação e permitir o uso da plataforma de relatórios de medicamentos.',
 situation='A indicação foi apresentada em 11 de março de 2025. O expediente registra leitura e despacho à Secretaria Executiva. O cadastro consultado ainda a identifica como em tramitação.',
 result='Há comprovação do pedido parlamentar. As fontes consultadas não comprovam assinatura de acordo entre os entes nem adesão operacional das três cidades à plataforma.',
 execution='Execução não confirmada nas fontes consultadas. Para demonstrá-la, seriam necessários registros do órgão responsável, como termo de cooperação ou relatório de implantação. Isso não significa que a medida não ocorreu.',
 events=[('2025-03-11','11 de março de 2025','Apresentação da indicação no SAPL.',1),('2025-03-11','11 de março de 2025','Expediente registra leitura e despacho à Secretaria Executiva.',2),('2026-09-10','Consulta em 10 de setembro de 2026','Cadastro consultado: em tramitação.',1)],
 sources=[('Texto original da Indicação nº 43/2025','https://sapl.al.ac.leg.br/media/sapl/public/materialegislativa/2025/16820/ind-n-43-andre_vale.pdf'),('Cadastro da Indicação nº 43/2025','https://sapl.al.ac.leg.br/materia/16820'),('Registro da indicação no expediente','https://sapl.al.ac.leg.br/sessao/expedientemateria/244')], refs=[0,0,2,1,1]),
 dict(slug='meu-amerlan', title='Sistema Meu Amer.Lan', category='MEMÓRIA E RECONHECIMENTO', document='Lei nº 4.606/2025 • origem: PL 37/2025', status='Lei publicada', kind='law',
 intro='Denominação legal do sistema de digitalização da Vigilância Sanitária do Estado.',
 problem='A iniciativa trata de reconhecimento e memória: atribuir ao sistema uma denominação em homenagem aos profissionais Amerval Soares Maia e Allan Vale Rogério dos Santos.',
 action='André é identificado como autor do PL 37/2025, que deu origem à Lei nº 4.606. A norma denomina o sistema Meu Amer.Lan e prevê sua identidade visual.',
 situation='A lei é datada de 15 de julho de 2025. O portal legislativo registra publicação no Diário Oficial nº 14.065, em 16 de julho de 2025. O texto prevê vigência a partir da publicação.',
 result='O resultado legislativo comprovado é a publicação da lei de denominação. A aprovação do projeto avançou, portanto, até uma norma publicada.',
 execution='A lei não comprova criação, pelo deputado, de aplicativo para consulta de estoques de medicamentos. A implantação operacional do sistema e os resultados de atendimento exigem documentação administrativa própria, não localizada nesta verificação.',
 events=[('2025-04-08','8 de abril de 2025','Apresentação do PL 37/2025.',1),('2025-07-15','15 de julho de 2025','Data da Lei nº 4.606.',0),('2025-07-16','16 de julho de 2025','Publicação no DOE nº 14.065.',0)],
 sources=[('Lei nº 4.606/2025: autoria, texto e publicação','https://app.al.ac.leg.br/legisla-e/legislacao/visualizar/9583'),('Identificação do PL 37/2025 no SAPL','https://sapl.al.ac.leg.br/relatorios/17079/etiqueta-materia-legislativa')], refs=[0,0,0,0,0]),
]

records.append(dict(slug='balanco-do-mandato', title='Balanço informado pela campanha', category='PRESTAÇÃO DE INFORMAÇÕES', document='Material da campanha • recebido em 10/09/2026', status='Documentação de execução pendente', kind='campaign',
 intro='Informações enviadas para o site sobre saúde, produção rural, infraestrutura, segurança e esporte.',
 problem='O material reúne ações em diferentes regiões e áreas. Não identifica, para cada uma, o período, instrumento orçamentário ou estágio da despesa.',
 action='A campanha informa mais de R$ 3 milhões destinados à saúde ao longo de três mandatos; contribuição para um aparelho de ressonância no Alto Acre; e indicações para serviços de saúde em Rio Branco.',
 situation='Também informa R$ 850 mil para agricultura familiar em Senador Guiomard, R$ 500 mil para equipamentos rurais no Juruá, R$ 250 mil para água encanada na Comunidade do Profeta, em Rodrigues Alves, e apoio a mais de 30 famílias produtoras de hortaliças no Bujari. Os valores não foram somados porque pode haver sobreposição.',
 result='Há ainda relatos de fiscalização e cobrança sobre a BR-364 e ramais, investimentos para a Polícia Militar em Cruzeiro do Sul e apoio a atividades esportivas. Esses resultados são declarações do material enviado, não execução comprovada por documentação nesta página.',
 execution='Para verificar cada entrega, faltam referências de emendas ou convênios, valores empenhados e pagos, datas, órgão executor e documentos de recebimento ou funcionamento. Fiscalizar ou solicitar uma obra não equivale a executá-la. A página será revisada quando esses registros forem apresentados.',
 events=[('2026-09-10','10 de setembro de 2026','Recebimento do balanço para inclusão no site; comprovação documental de cada entrega pendente.',0)],
 sources=[('Registro do material fornecido — não é documento de execução','/arquivos/balanco-informado.txt')], refs=[0,0,0,0,0]))

header = re.search(r'<header class="site-header".*?</header>', home, re.S).group()
footer = home[home.index('  <footer'):home.index('</body>')]
def absolute_links(s):
    s = re.sub(r'(href|src)="(assets/[^"\s]+)"', r'\1="/\2"', s)
    return re.sub(r'href="#(inicio|sobre|trajetoria|atuacao|contato)"', r'href="/#\1"', s)
header, footer = absolute_links(header), absolute_links(footer)
for item in records:
    def source_link(i):
        title,url=item['sources'][i]
        return f'<a class="evidence-link" href="{escape(url,quote=True)}" target="_blank" rel="noopener noreferrer">{escape(title)} ↗</a>'
    blocks=''
    for index,(key,title) in enumerate([('problem','O problema ou objetivo'),('action','A ação do deputado'),('situation','Situação verificada'),('result','O que está comprovado'),('execution','Execução e limites da evidência')]):
        blocks+=f'<section class="evidence-block" id="{key}"><span class="evidence-index">0{index+1}</span><div><h2>{title}</h2><p>{escape(item[key])}</p>{source_link(item["refs"][index])}</div></section>'
    events=''.join(f'<li><time datetime="{dt}">{label}</time><p>{escape(desc)}</p>{source_link(ref)}</li>' for dt,label,desc,ref in item['events'])
    sources=''.join(f'<li>{source_link(i)}</li>' for i in range(len(item['sources'])))
    related=''.join(f'<a href="/atuacao/{r["slug"]}/">{escape(r["title"])} <span aria-hidden="true">↗</span></a>' for r in records if r is not item)
    html=f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(item['title'])} | Atuação de André Vale</title><meta name="description" content="{escape(item['intro'],quote=True)} Situação: {escape(item['status'],quote=True)}.">
<meta name="theme-color" content="#252465"><link rel="canonical" href="https://andredrogavale11444.com.br/atuacao/{item['slug']}/">
<meta property="og:title" content="{escape(item['title'],quote=True)} | André Vale"><meta property="og:description" content="{escape(item['status'],quote=True)}. Conheça a iniciativa e consulte as fontes oficiais."><meta property="og:type" content="article"><meta property="og:locale" content="pt_BR">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="preload" as="font" href="/assets/fonts/manrope-variable.woff2" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css?v=visual-2"><link rel="stylesheet" href="/refinement.css?v=visual-2"><link rel="stylesheet" href="/initiatives.css?v=1"><script src="/script.js" defer></script></head>
<body class="initiative-page"><a class="skip-link" href="#conteudo">Pular para o conteúdo</a>{header}
<main id="conteudo"><div class="container"><nav class="breadcrumbs" aria-label="Caminho da página"><a href="/">Início</a><span aria-hidden="true">/</span><a href="/#atuacao">Atuação</a></nav>
<div class="evidence-heading"><p class="eyebrow blue">{item['category']}</p><span class="status-badge {item['kind']}">{item['status']}</span><h1>{item['title']}</h1><p class="evidence-intro">{item['intro']}</p><div class="evidence-meta"><span>{item['document']}</span><span>Verificado em <time datetime="2026-09-10">10/09/2026</time></span></div></div>
<div class="evidence-layout"><div>{blocks}</div><aside class="evidence-sidebar" aria-labelledby="events-title"><h2 id="events-title">Registros no tempo</h2><ol>{events}</ol><p class="evidence-note">Situação baseada nos registros consultados. Esta página não recebe atualizações automáticas dos órgãos públicos.</p></aside></div>
<section class="evidence-sources" aria-labelledby="sources-title"><h2 id="sources-title">{'Origem das informações' if item['kind']=='campaign' else 'Fontes oficiais'}</h2><ul>{sources}</ul><p>“Não confirmado” indica ausência de comprovação nas fontes consultadas, não uma conclusão de que a ação não aconteceu.</p></section>
<nav class="related-initiatives" aria-label="Outras iniciativas"><h2>Continue acompanhando</h2>{related}<a href="/#atuacao">Voltar para todas as iniciativas <span aria-hidden="true">←</span></a></nav></div></main>{footer}</body></html>'''
    folder=PUBLIC/'atuacao'/item['slug'];folder.mkdir(parents=True,exist_ok=True)
    (folder/'index.html').write_text(html,encoding='utf-8')

# Keep the existing accordions and attach the new evidence pages to each one.
def update_card(match):
    card=match.group(0)
    for item in records:
        if f'<strong>{item["title"]}</strong>' not in card: continue
        card=re.sub(r'<small>.*?</small>', f'<small>{item["status"].upper()}</small>',card,count=1)
        card=re.sub(r'<span class="document-tag">.*?</span>',f'<span class="document-tag">{item["document"]}</span>',card,count=1)
        if item['kind']=='law':
            card=re.sub(r'<p>Propôs dar o nome.*?</p>', '<p>O PL 37/2025 deu origem à Lei nº 4.606, de 15 de julho de 2025, publicada no dia seguinte. A norma denomina o sistema de digitalização da Vigilância Sanitária Meu Amer.Lan.</p>',card,count=1)
        if item['kind']=='project':
            card=re.sub(r'<p class="document-note">.*?</p>','<p class="document-note">O projeto recebeu o Veto nº 11/2026. O cadastro do veto consta em tramitação na consulta de 10/09/2026; não foi confirmada publicação de lei decorrente deste projeto.</p>',card,count=1)
        if 'class="initiative-detail-link"' not in card:
            card=card.replace('</div></details>', f'<a class="initiative-detail-link" href="/atuacao/{item["slug"]}/">Entenda a iniciativa e sua situação <span aria-hidden="true">↗</span></a></div></details>')
    return card
home=re.sub(r'<details class="initiative">.*?</details>',update_card,home,flags=re.S)
if 'href="initiatives.css?v=1"' not in home:
    home=home.replace('<script src="script.js" defer></script>','<link rel="stylesheet" href="initiatives.css?v=1">\n  <script src="script.js" defer></script>')
home=home.replace('É um registro de sua atividade legislativa; a apresentação do projeto não comprova sua transformação em lei.', 'O projeto recebeu o Veto nº 11/2026. Na consulta de 10/09/2026, o veto consta em tramitação. <a href="/atuacao/inspecoes-com-aviso-previo/">Veja a situação documentada</a>.')
legend='''<dl class="status-guide"><div><dt>Pedido</dt><dd>Solicitação ao órgão responsável.</dd></div><div><dt>Projeto</dt><dd>Proposta legislativa; aprovação não comprova execução.</dd></div><div><dt>Lei</dt><dd>Norma com publicação identificada.</dd></div><div><dt>Execução</dt><dd>Implementação demonstrada por registros próprios.</dd></div></dl>'''
if 'class="status-guide"' not in home:
    home=home.replace('<div class="initiatives">', '<div class="initiatives">'+legend,1)
(PUBLIC/'index.html').write_text(home,encoding='utf-8')
if '/atuacao/balanco-do-mandato/' not in home:
    home=home.replace('<div class="initiatives">','<div class="initiatives"><a class="campaign-balance-link" href="/atuacao/balanco-do-mandato/">Balanço enviado pela campanha <span>Valores e ações informados • documentação de execução pendente ↗</span></a>',1)
    (PUBLIC/'index.html').write_text(home,encoding='utf-8')
print(f'Generated {len(records)} evidence pages and updated home summaries.')
