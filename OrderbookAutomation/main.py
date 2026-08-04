from __future__ import annotations


from config import get_default_config
from modules.derived_dataset_manager import run_phase2
from modules.dictionary_builder import build_data_dictionary_markdown
from modules.loader import load_workbooks
from modules.profiler import build_workbook_profiles, write_workbook_profile
from modules.utils import Timer, ensure_directory, setup_logging
from modules.validator import DataValidationError, validate_loaded_workbooks
from modules.workbook_manager import build_join_key_analysis_markdown, discover_join_key_candidates


def run_phase1() -> None:
    """Run Phase 1 ingestion only: load, validate, profile, dictionary, join-key analysis."""
    config = get_default_config()

    ensure_directory(config.output_dir)
    ensure_directory(config.logs_dir)
    ensure_directory(config.docs_dir)

    logger = setup_logging(config.logs_dir, log_name="phase1.log")

    with Timer() as timer:
        logger.info("Starting Phase 1 ingestion workflow")

        loaded_workbooks = load_workbooks(config, logger)
        validation_result = validate_loaded_workbooks(config, loaded_workbooks, logger)

        summary_df, columns_df = build_workbook_profiles(loaded_workbooks, logger)
        profile_path = config.output_dir / "Workbook_Profile.xlsx"
        write_workbook_profile(summary_df, columns_df, profile_path, logger)

        dictionary_markdown = build_data_dictionary_markdown(loaded_workbooks, config.join_key_hints)
        dictionary_path = config.docs_dir / "DATA_DICTIONARY.md"
        dictionary_path.write_text(dictionary_markdown, encoding="utf-8")
        logger.info("Wrote data dictionary to %s", dictionary_path)

        key_candidates = discover_join_key_candidates(loaded_workbooks, config.join_key_hints, logger)
        join_key_markdown = build_join_key_analysis_markdown(key_candidates)
        join_key_path = config.docs_dir / "JOIN_KEY_ANALYSIS.md"
        join_key_path.write_text(join_key_markdown, encoding="utf-8")
        logger.info("Wrote join key analysis to %s", join_key_path)

        if validation_result.has_errors:
            raise DataValidationError("Phase 1 validation failed. Review logs/phase1.log for details.")

        phase2_result = run_phase2(loaded_workbooks, config, logger, timer.elapsed_seconds)
        logger.info("Phase 2 completed successfully. Derived workbook saved to %s", phase2_result.output_path)

        logger.info("Phase 1 completed successfully in %.2f seconds", timer.elapsed_seconds)


if __name__ == "__main__":
    run_phase1()
