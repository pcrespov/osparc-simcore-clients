"""
0.5.0 osparc client
"""
from typing import Tuple

from osparc_client import (  # APIs; API client; models
    ApiClient,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    BodyUploadFileV0FilesContentPut,
    Configuration,
    ErrorGet,
    File,
    FilesApi,
    Groups,
    HTTPValidationError,
    Job,
    JobInputs,
    JobMetadata,
    JobMetadataUpdate,
    JobOutputs,
    JobStatus,
    LimitOffsetPageFile,
    LimitOffsetPageJob,
    LimitOffsetPageSolver,
    LimitOffsetPageStudy,
    Links,
    Meta,
    MetaApi,
    OnePageSolverPort,
    OnePageStudyPort,
    OpenApiException,
    Profile,
    ProfileUpdate,
)
from osparc_client import RunningState as TaskStates
from osparc_client import (  # APIs; API client; models
    Solver,
    SolverPort,
    SolversApi,
    StudiesApi,
    Study,
    StudyPort,
    UserRoleEnum,
    UsersApi,
    UsersGroup,
    ValidationError,
    __version__,
)

from ._info import openapi

__all__: Tuple[str, ...] = (
    # imports from osparc_client
    "__version__",
    "FilesApi",
    "MetaApi",
    "SolversApi",
    "UsersApi",
    "BodyUploadFileV0FilesContentPut",
    "File",
    "Groups",
    "HTTPValidationError",
    "Job",
    "JobInputs",
    "JobOutputs",
    "JobStatus",
    "Meta",
    "Profile",
    "ProfileUpdate",
    "Solver",
    "TaskStates",
    "UserRoleEnum",
    "UsersGroup",
    "ValidationError",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiException",
    "StudiesApi",
    "OnePageSolverPort",
    "StudyPort",
    "Study",
    "LimitOffsetPageStudy",
    "LimitOffsetPageFile",
    "JobMetadataUpdate",
    "LimitOffsetPageJob",
    "Links",
    "SolverPort",
    "JobMetadata",
    "LimitOffsetPageSolver",
    "ErrorGet",
    "OnePageStudyPort",
    # imports from osparc
    "openapi",
)
