# Script Principal - Aplicar Todas as Otimizações
# Execute este script para aplicar todas as configurações de uma vez

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    GTA V & FIVEM FPS OPTIMIZER" -ForegroundColor Green
Write-Host "    CONFIGURAÇÃO PROFISSIONAL" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se está executando como administrador
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

if (-not $isAdmin) {
    Write-Host "⚠️  AVISO: Execute como Administrador para melhores resultados!" -ForegroundColor Red
    Write-Host ""
}

Write-Host "🎮 Aplicando otimizações para GTA V..." -ForegroundColor Green
& "$PSScriptRoot\gta_v_fps_optimizer.ps1"

Write-Host ""
Write-Host "🏁 Aplicando otimizações para FiveM..." -ForegroundColor Green
& "$PSScriptRoot\fivem_fps_optimizer.ps1"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ TODAS AS OTIMIZAÇÕES APLICADAS!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📋 RESUMO DAS OTIMIZAÇÕES:" -ForegroundColor Yellow
Write-Host ""
Write-Host "GTA V:" -ForegroundColor Cyan
Write-Host "  ✓ settings.xml otimizado para máximo FPS" -ForegroundColor White
Write-Host "  ✓ commandline.txt com parâmetros de performance" -ForegroundColor White
Write-Host "  ✓ Backup dos arquivos originais criado" -ForegroundColor White
Write-Host ""
Write-Host "FiveM:" -ForegroundColor Cyan
Write-Host "  ✓ performance.cfg criado" -ForegroundColor White
Write-Host "  ✓ Launcher otimizado na área de trabalho" -ForegroundColor White
Write-Host "  ✓ Configurações específicas para combate" -ForegroundColor White
Write-Host ""

Write-Host "🎯 CONFIGURAÇÕES PARA COMBATE COMPETITIVO:" -ForegroundColor Yellow
Write-Host "  • Todas as configurações gráficas no MÍNIMO" -ForegroundColor White
Write-Host "  • Sombras, reflexões e efeitos DESABILITADOS" -ForegroundColor White
Write-Host "  • Densidade de NPCs e veículos no MÍNIMO" -ForegroundColor White
Write-Host "  • Motion blur e efeitos visuais REMOVIDOS" -ForegroundColor White
Write-Host "  • VSync DESABILITADO para menor input lag" -ForegroundColor White
Write-Host "  • Configurações de CPU e GPU OTIMIZADAS" -ForegroundColor White
Write-Host ""

Write-Host "🚀 PRÓXIMOS PASSOS:" -ForegroundColor Green
Write-Host "1. REINICIE o GTA V completamente" -ForegroundColor White
Write-Host "2. Para FiveM, use o launcher FiveM_Performance.bat" -ForegroundColor White
Write-Host "3. Verifique se o FPS melhorou nos assaltos" -ForegroundColor White
Write-Host "4. Se precisar reverter, use os backups criados" -ForegroundColor White
Write-Host ""

Write-Host "⚡ DICAS EXTRAS PARA MÁXIMO FPS:" -ForegroundColor Yellow
Write-Host "• Feche outros programas enquanto joga" -ForegroundColor White
Write-Host "• Use modo de energia 'Alto desempenho'" -ForegroundColor White
Write-Host "• Mantenha drivers da GPU atualizados" -ForegroundColor White
Write-Host "• Considere overclock na GPU se souber fazer" -ForegroundColor White
Write-Host ""

Write-Host "🎮 BOA SORTE NOS ASSALTOS! 🎮" -ForegroundColor Green -BackgroundColor Black
Write-Host ""

# Perguntar se quer abrir a pasta de backup
$response = Read-Host "Deseja abrir a pasta com os backups? (s/n)"
if ($response -eq 's' -or $response -eq 'S') {
    $backupPath = "$env:USERPROFILE\Documents\Rockstar Games\GTA V"
    if (Test-Path $backupPath) {
        Start-Process explorer.exe $backupPath
    }
}

Write-Host "Pressione qualquer tecla para sair..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")