<!--
---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
subcategory: "Life Sciences"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to life_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [genetics, genomics, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Genética y Genómica
La genética es el estudio de la herencia: cómo se transmiten los rasgos de padres a hijos a través del ADN. La genómica es el estudio de genomas completos: todos los genes, las regiones no codificantes, cómo interactúan y cómo varían entre individuos y poblaciones. La transición de la genética a la genómica fue impulsada por la tecnología de secuenciación: pasamos de estudiar un gen a la vez a leer genomas completos en horas, generando datos que están transformando la medicina, la agricultura, la ciencia forense y nuestra comprensión de la evolución.
---

## Fundamentos del ADN
### Estructura del ADN
| Componente | Descripción |
|-----------|-------------|
| **Nucleótido** | Bloque de construcción del ADN; consta de un azúcar (desoxirribosa), un grupo fosfato y una base nitrogenada |
| **Bases** | Adenina (A), Timina (T), Guanina (G), Citosina (C) |
| **Emparejamiento de bases** | A se empareja con T (2 enlaces de hidrógeno); G se empareja con C (3 enlaces de hidrógeno) |
| **Doble hélice** | Dos hebras que corren en sentido antiparalelo (5' a 3' y 3' a 5'); retorcido en forma de hélice |
| **Cromosoma** | Una única y larga molécula de ADN envuelta alrededor de proteínas histonas; los humanos tenemos 46 (23 pares) |
| **Genoma** | El conjunto completo de ADN de un organismo; genoma humano tiene ~3.200 millones de pares de bases |
### Dogma Central de la Biología Molecular
| Paso | Proceso | Ubicación | Producto |
|------|---------|----------|---------|
| **Replicación** | ADN → ADN | Núcleo | Dos moléculas de ADN idénticas |
| **Transcripción** | ADN → ARNm | Núcleo | ARN mensajero |
| **Traducción** | ARNm → proteína | Ribosoma (citoplasma) | Cadena polipeptídica (proteína) |
---

## Expresión genética
### Cómo se regulan los genes
| Nivel | Mecanismo | Ejemplo |
|-------|-----------|---------|
| **Epigenético** | metilación del ADN; modificación de histonas; remodelación de la cromatina | Silenciamiento de un cromosoma X en mujeres |
| **Transcripcional** | Los factores de transcripción se unen a promotores/potenciadores; activar o reprimir | operón lac en bacterias; genes que responden a hormonas |
| **Postranscripcional** | Empalme alternativo; estabilidad del ARNm; microARN | Un gen → múltiples variantes de proteínas |
| **Traduccional** | Disponibilidad de ribosomas; regulación del factor de iniciación | Regulación del hierro mediante ARNm de ferritina |
| **Postraduccional** | Modificación de proteínas (fosforilación, ubiquitinación); degradación | Control del ciclo celular |
---

## Patrones de herencia
### Genética mendeliana
| Patrón | Descripción | Ejemplo |
|---------|-------------|---------|
| **Autosómico dominante** | Una copia del alelo es suficiente | enfermedad de Huntington; acondroplasia |
| **Autosómico recesivo** | Se requieren dos copias | Fibrosis quística; anemia falciforme |
| **Dominante ligado al cromosoma X** | Gen en el cromosoma X; una copia suficiente | Síndrome de Rett |
| **Resesivo ligado al cromosoma X** | Gen en el cromosoma X; varones más afectados | Hemofilia; daltonismo |
| **Codominancia** | Ambos alelos se expresan por igual | Grupos sanguíneos ABO (A y B) |
| **Dominio incompleto** | El heterocigoto es intermedio | Flores rosadas de padres rojos y blancos |
| **Poligénico** | Múltiples genes contribuyen a un rasgo | Altura; color de piel; inteligencia |
| **Pleiotropía** | Un gen afecta múltiples rasgos | Síndrome de Marfan (tejido conectivo, ojos, corazón) |
---

## Genómica
### Tipos de genómica
| Tipo | Enfoque | Solicitud |
|------|-------|-------------|
| **Genómica estructural** | Estructura 3D de todas las proteínas del genoma | Diseño de fármacos; ingeniería de proteínas |
| **Genómica funcional** | Qué hacen los genes; interacciones genéticas; patrones de expresión | Comprender los mecanismos de la enfermedad |
| **Genómica comparada** | Comparación de genomas entre especies | Relaciones evolutivas; identificación de regiones conservadas |
| **Metagenómica** | ADN de muestras ambientales (no cultivadas) | Estudios de microbioma; descubriendo nuevos organismos |
| **Farmacogenómica** | Cómo los genes afectan la respuesta a los medicamentos | Medicina personalizada; dosificación de medicamentos |
| **Epigenómica** | Modificaciones epigenéticas de todo el genoma | Diagnóstico de cáncer; biología del desarrollo |
### Tecnologías de secuenciación de ADN
| Generación | Tecnología | Longitud de lectura | Rendimiento | Característica clave |
|-----------|-----------|-------------|------------|-------------|
| **Primera generación** | Secuenciación de Sanger | ~1.000 pb | Bajo | Precisión estándar de oro; utilizado para la validación |
| **Segunda generación** | Illumina (Solexa) | 50–300 pb | Muy alto | Lecturas cortas; plataforma dominante; bajo coste por base |
| **Segunda generación** | Torrente de iones | 200–400 pb | Alto | Basado en semiconductores; sin óptica |
| **Tercera generación** | PacBio (SMRT) | 10.000-100.000 pb | Moderado | Lecturas largas; resuelve regiones repetitivas |
| **Tercera generación** | Nanoporo Oxford | Hasta millones de pb | Moderado a alto | Lecturas ultralargas; portátil (MinION); en tiempo real |
---

## Variación genética
### Tipos de variación
| Tipo | Descripción | Frecuencia |
|------|-------------|-----------|
| **SNP** (polimorfismo de un solo nucleótido) | Cambio de base única | Más común; ~1 de cada 1.000 bases |
| **Inserción/Eliminación (indel)** | Adición o eliminación de bases | Puede causar mutaciones por desplazamiento de marco |
| **CNV** (Variación del número de copias) | Segmentos duplicados o eliminados (1 kb – varios Mb) | Contribuye a la enfermedad y la evolución |
| **Variación estructural** | Inversiones; translocaciones; grandes reordenamientos | Menos común; puede ser patógeno |
| **Microsatélite (STR)** | Repeticiones cortas en tándem (repetidas de 2 a 6 pb) | Forense; pruebas de paternidad |
### GWAS (Estudios de asociación de todo el genoma)
| Paso | Descripción |
|------|-------------|
| **1. Recoger muestras** | Casos (con enfermedad) y controles (sin) |
| **2. Genotipo** | Utilice matrices de SNP para genotipar cientos de miles de variantes |
| **3. Prueba estadística** | Pruebe cada SNP para determinar su asociación con el rasgo |
| **4. Parcela de Manhattan** | Visualice resultados en todos los cromosomas |
| **5. Replicación** | Confirmar hallazgos en muestras independientes |
---

## Edición genética
### CRISPR-Cas9
| Componente | Función |
|-----------|----------|
| **ARN guía (ARNg)** | ~20 nucleótidos; coincide con la secuencia de ADN objetivo |
| **Proteína Cas9** | Tijeras moleculares; corta el ADN en el sitio objetivo |
| **Secuencia PAM** | Motivo corto (NGG) junto al objetivo; requerido para el enlace Cas9 |
| **HDR** (Reparación dirigida por homología) | Edición precisa utilizando una plantilla de donante |
| **NHEJ** (Unión de extremos no homólogos) | Reparación propensa a errores; crea inserciones/eliminaciones (knockout) |
### Aplicaciones de edición genética
| Solicitud | Descripción |
|-------------|-------------|
| **Terapéutico** | Corregir mutaciones que causan enfermedades (drepanocitosis; beta-talasemia) |
| **Agricultura** | Cultivos resistentes a enfermedades; ganadería mejorada |
| **Investigación** | Crear modelos impresionantes; función del gen del estudio |
| **Impulsor genético** | Difundir una modificación genética a través de una población (por ejemplo, mosquitos resistentes a la malaria) |
---

## Consideraciones éticas
| Problema | Preocupación |
|-------|---------|
| **Privacidad genética** | ¿A quién pertenecen los datos de su genoma? ¿Pueden utilizarlo los empleadores o las aseguradoras? |
| **Edición genética en embriones** | Cambios hereditarios; bebés de diseño; efectos no deseados fuera del objetivo |
| **Discriminación genética** | GINA (EE.UU.) protege contra cierta discriminación pero tiene lagunas |
| **Consentimiento informado** | Datos genómicos revelan información sobre familiares que no han dado su consentimiento |
| **Almacenamiento de datos** | Los genomas son grandes (~200 GB sin procesar); desafíos de seguridad y almacenamiento a largo plazo |
| **Patrimonio** | La medicina genómica corre el riesgo de ampliar las disparidades en salud si solo está disponible para las poblaciones ricas |
---

## Resumen
La genética estudia cómo funcionan y se heredan los genes individuales. La genómica estudia genomas completos: todos los genes, sus interacciones y su variación. El ADN se transcribe en ARN, que se traduce en proteínas. La expresión génica está regulada en múltiples niveles: epigenético, transcripcional, postranscripcional, traduccional y postraduccional. La herencia sigue patrones (dominantes, recesivos, poligénicos) que determinan cómo los rasgos pasan entre generaciones. Las tecnologías de secuenciación modernas (Illumina, PacBio, Nanopore) pueden leer genomas completos de forma rápida y económica. CRISPR-Cas9 permite la edición genética precisa con potencial transformador en medicina y agricultura. Los mayores desafíos son éticos: quién controla los datos genómicos, cómo regular la edición de genes en embriones y cómo garantizar que la medicina genómica beneficie a todos, no sólo a los privilegiados.